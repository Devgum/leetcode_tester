![img][pypi_version]

# leetcode_tester
在leetcode做题时，感觉提交代码时，效率受制于网络。Leetcode的编辑器环境也不是很顺手，常常急躁提交留下失败的提交记录。
遂简单写了个本地测试框架，方便在本地进行测试。

# 安装方法
```
pip install leetcode-tester
```

# 使用方法

## 使用示例

```
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

```

Solution类可以选择从Leetcode的编辑器中复制而来。当然，有些额外的特殊类型，还是需要自己补充。  
Tester的addTest方法用于添加用例，最后一个入参会被作为期待结果，之前的参数会被作为入参传入Solution方法。

## 输出示例

```
Input: [1, 2, 3]
Expect: [3]
Result: [3]
Status: [RIGHT]
Exception: [None]
Cost: [7.152557373046875e-06]

Input: [2, 4, 6]
Expect: [6]
Result: [6]
Status: [RIGHT]
Exception: [None]
Cost: [3.0994415283203125e-06]

{'TOTAL': 2, 'RIGHT': 2, 'WRONG': 0, 'EXCEPTION': 0, 'TOTAL_COST': 1.0251998901367188e-05}
```

# TODO

> 持续整理LeetCode中遇到的额外类型，例如：ListNode、TreeNode，并将其固化在这个包里以供用户直接使用。  

[pypi_version]: https://img.shields.io/pypi/v/leetcode-tester.svg?style=flat
