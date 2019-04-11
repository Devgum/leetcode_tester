# coding:utf-8

import time
from operator import eq


def timer(func):
    def new_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        cost = time.time() - start
        print(f'{func.__name__} cost: [{cost}]')
        return result
    return new_func


class Tester():
    def __init__(self, solution_func):
        self.solution_func = solution_func
        self.test_args = []
        self.expect = []

    def addTest(self, *args):
        self.test_args.append(args[:-1])
        self.expect.append(args[-1])

    @timer
    def doTest(self):
        failed = 0
        for i in range(len(self.expect)):
            args = self.test_args[i]
            expect = self.expect[i]
            result = self.solution_func(*args)
            print(f'Test [{i}]:')
            print(f"Args: [{', '.join(str(arg) for arg in args)}]")
            print(f'Expect: [{expect}]')
            print(f'Result: [{result}]')
            print(f'Succeed: [{eq(result, expect)}]')
            print(f'==============')
            if result != expect:
                failed += 1
        print(f'Test finished.')
        print(f'[{failed}] failed. [{len(self.expect) - failed}] succeed.')
