# coding:utf-8

import time
import asyncio
from enum import Enum
from operator import eq
from functools import partial
from concurrent.futures import ProcessPoolExecutor


class CaseStatus(Enum):
    RIGHT = 1
    WRONG = 2
    EXCEPTION = 3
    PROCESSING = 4
    PENDING = 5


class Case:
    def __init__(self, *args):
        if len(args) < 1:
            raise Exception(f'Invalid Case.')
        self.case_args = list(args[:-1])
        self._case_args_str = ', '.join([str(arg) for arg in args[:-1]])
        self.expect = args[-1]
        self.result = None
        self.status = CaseStatus.PENDING
        self.exception = None
        self.cost = 0

    def check_result(self, result):
        return eq(self.expect, result)

    def do(self, solution_func):
        self.status = CaseStatus.PROCESSING
        try:
            start = time.time()
            self.result = solution_func(*self.case_args)
            self.cost = time.time() - start
        except Exception as e:
            self.status = CaseStatus.EXCEPTION
            self.exception = e
        else:
            if self.check_result(self.result):
                self.status = CaseStatus.RIGHT
            else:
                self.status = CaseStatus.WRONG
        return self

    def __str__(self):
        return (
            f'Input: [{self._case_args_str}]\n'
            f'Expect: [{self.expect}]\n'
            f'Result: [{self.result}]\n'
            f'Status: [{self.status.name}]\n'
            f'Exception: [{self.exception}]\n'
            f'Cost: [{self.cost}]\n'
        )


class TestResult:
    def __init__(self, result_cases):
        self.cases = result_cases
        self.stat = {'TOTAL': len(self.cases)}
        for status in [CaseStatus.RIGHT,
                       CaseStatus.WRONG,
                       CaseStatus.EXCEPTION]:
            self.stat[status.name] = 0
        cost_count = 0
        for case in self.cases:
            self.stat[case.status.name] += 1
            cost_count += case.cost
        self.stat['TOTAL_COST'] = cost_count

    def statistics(self):
        return dict(self.stat)

    def show(self):
        for case in self.cases:
            print(case)
        print(self.statistics())


class Tester:
    def __init__(self, solution_func, process_pool_size: int = None):
        self.solution_func = solution_func
        if process_pool_size:
            self.executor = ProcessPoolExecutor(process_pool_size)
        else:
            self.executor = ProcessPoolExecutor()
        self.cases = []

    def addTest(self, *args):
        self.cases.append(Case(*args))

    def doTest(self, show=True):
        loop = asyncio.get_event_loop()
        all_task = []
        for case in self.cases:
            case_task = loop.run_in_executor(
                self.executor, partial(case.do, self.solution_func))
            all_task.append(case_task)
        result = loop.run_until_complete(asyncio.gather(*all_task))
        result = TestResult(result)
        if show:
            result.show()
        return result
