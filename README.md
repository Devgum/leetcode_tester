# leetcode_tester
在leetcode做题时，感觉提交代码时，效率受制于网络。Leetcode的编辑器环境也不是很顺手，常常急躁提交留下失败的提交记录。
遂简单写了个本地测试框架，方便在本地进行测试。

# 使用方法

可以参见示例

```
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

```

Solution类可以选择从Leetcode的编辑器中复制而来。当然，有些额外的特殊类型，还是需要自己补充。