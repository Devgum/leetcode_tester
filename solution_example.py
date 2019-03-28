# coding:utf-8

from leetcode_tester import Tester


class Solution():
    def sfc(self, *args):
        # TODO: write your code here
        # Example:
        return sum(args)


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.sfc)
    # TODO: add test case here
    # Example:
    test.addTest(1, 2, 3)
    test.addTest(2, 4, 6)
    test.doTest()
