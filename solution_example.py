from leetcode_tester.tester import Tester


class SolutionExample():
    def sfc(self, *args):
        # TODO: write your code here
        # Example: 
        return sum(args)


if __name__ == '__main__':
    solution = SolutionExample()
    test = Tester(solution.sfc)
    # TODO: add test case here
    # Example: 
    test.addTest(1, 2, 3)
    test.doTest()
