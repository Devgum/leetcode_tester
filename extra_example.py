# coding:utf-8

from leetcode_tester import Tester, ListNode
# from leetcode_tester import ListNode


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
