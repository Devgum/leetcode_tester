# coding:utf-8

from leetcode_tester import Tester


class ListNode:
    '''
    如果涉及特殊类型，需要自定义
    '''

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        '''
        实现特殊类型的__str__方法
        以便可以更好地在结果中进行展示
        '''
        result = f'{self.val}'
        if self.next:
            result = f'{result} -> {self.next}'
        return result

    def __eq__(self, node):
        '''
        若结果也是特殊类型
        需要实现__eq__方法
        '''
        if not isinstance(node, self.__class__):
            return False
        return self.val.__eq__(node.val) and self.next.__eq__(node.next)

    @classmethod
    def init_with_list(cls, value_list):
        '''
        用于快速创建链表
        以便创建用例
        '''
        if not value_list:
            return None
        if not isinstance(value_list, list):
            return ListNode(value_list)
        root_node = ListNode(value_list[0])
        pre_node = root_node
        for value in value_list[1:]:
            pre_node.next = ListNode(value)
            pre_node = pre_node.next
        return root_node


class Solution:
    '''
    LeetCode No.2 [Add Two Numbers]
    '''

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # TODO: write your code here
        # Example:
        zero = current = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            val = v1 + v2 + carry
            carry = val // 10

            current.next = ListNode(val % 10)
            current = current.next

        return zero.next


if __name__ == '__main__':
    solution = Solution()
    test = Tester(solution.addTwoNumbers)
    test.addTest(
        ListNode.init_with_list([2, 4, 3]),
        ListNode.init_with_list([5, 6, 4]),
        ListNode.init_with_list([7, 0, 8]))
    test.addTest(
        ListNode.init_with_list([1, 1, 9]),
        ListNode.init_with_list([0, 0, 1]),
        ListNode.init_with_list([1, 1, 0, 1]))
    test.addTest(
        ListNode.init_with_list([1, 1]),
        ListNode.init_with_list([0]),
        ListNode.init_with_list([1, 1]))
    test.addTest(
        ListNode.init_with_list([0]),
        ListNode.init_with_list([1, 1]),
        ListNode.init_with_list([1, 1]))
    test.addTest(
        ListNode.init_with_list([]),
        ListNode.init_with_list([1, 1]),
        ListNode.init_with_list([1, 1]))
    test.addTest(
        ListNode.init_with_list([1, 1]),
        ListNode.init_with_list([]),
        ListNode.init_with_list([1, 1]))
    test.addTest(
        ListNode.init_with_list([]),
        ListNode.init_with_list([]),
        ListNode.init_with_list([]))
    test.doTest()
