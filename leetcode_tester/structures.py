# coding:utf-8


class Node:

    def __init__(self, x):
        self. val = x

    def __str__(self):
        return str(self.val)


class ListNode(Node):

    def __init__(self, x):
        super().__init__(x)
        self.next = None

    def __str__(self):
        result = f'{self.val}'
        if self.next:
            result = f'{result} -> {self.next}'
        return result

    def __eq__(self, node):
        if not isinstance(node, self.__class__):
            return False
        return self.val.__eq__(node.val) and self.next.__eq__(node.next)

    @classmethod
    def init_with_list(cls, value_list):
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

