'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''


# Definition for singly-linked list.
class ListNode(object):
    val = 0
    next_node = None

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node

    def print_nodes(self):
        print(self.val, end=" ")
        next_node = self.next_node
        while next_node is not None:
            print(next_node.val, end=" ")
            next_node = next_node.next_node
        print("")

    def insert_node(self, next_node):
        self.next_node = next_node


class Solution(object):
    def add_two_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ln1 = l1
        ln2 = l2
        carry_over = 0

        sum_list = None
        sum_list_ptr = None
        while (ln1 is not None) or (ln2 is not None):
            v1 = 0
            v2 = 0
            if ln1 is not None:
                v1 = ln1.val
                ln1 = ln1.next_node
            if ln2 is not None:
                v2 = ln2.val
                ln2 = ln2.next_node

            sum_val = v1 + v2 + carry_over
            val = sum_val % 10
            if sum_val >= 10:
                carry_over = 1
            else:
                carry_over = 0

            if sum_list is None:
                sum_list = ListNode(val)
                sum_list_ptr = sum_list
            else:
                sum_list_ptr.insert_node(ListNode(val))
                sum_list_ptr = sum_list_ptr.next_node

        if carry_over != 0:
            sum_list_ptr.insert_node(ListNode(carry_over))

        return sum_list


l1_n_1 = ListNode(2)
l1_n_2 = ListNode(4)
l1_n_3 = ListNode(3)

l1_n_1.insert_node(l1_n_2)
l1_n_2.insert_node(l1_n_3)
l1_n_1.print_nodes()

l2_n_1 = ListNode(5)
l2_n_2 = ListNode(6)
l2_n_3 = ListNode(4)

l2_n_1.insert_node(l2_n_2)
l2_n_2.insert_node(l2_n_3)
l2_n_1.print_nodes()


sol = Solution()

new_list = sol.add_two_lists(l1_n_1, l2_n_1)
new_list.print_nodes()

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

l3_n_1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l3_n_1.print_nodes()
l4_n_1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
l4_n_1.print_nodes()

new_list_2 = sol.add_two_lists(l3_n_1, l4_n_1)
new_list_2.print_nodes()