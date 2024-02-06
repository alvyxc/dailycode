from BinaryTree import BinaryTreeNode
'''
Given a binary search tree and a range [a, b] (inclusive), return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).
'''


def get_bst_sum_from_range(range_pair, tree_node):
    """
    :type range_pair: Pair
    :type tree_node: BinaryTreeNode
    :rtype: int
    """
    if tree_node is None:
        return 0

    node_val = 0

    if range_pair[0] <= tree_node.data <= range_pair[1]:
        node_val = tree_node.data

    # search
    if range_pair[0] <= tree_node.data <= range_pair[1]:
        return node_val + get_bst_sum_from_range(range_pair, tree_node.leftChild) + get_bst_sum_from_range(range_pair, tree_node.rightChild)
    elif range_pair[0] <= tree_node.data:
        return node_val + get_bst_sum_from_range(range_pair, tree_node.leftChild)
    elif range_pair[1] >= tree_node.data:
        return node_val + get_bst_sum_from_range(range_pair, tree_node.rightChild)
    else:
        return 0
    

node1 = BinaryTreeNode(5)
node2 = BinaryTreeNode(3)
node3 = BinaryTreeNode(8)
node4 = BinaryTreeNode(2)
node5 = BinaryTreeNode(4)
node6 = BinaryTreeNode(6)
node7 = BinaryTreeNode(10)

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7

p = (4, 9)
print("tree range [4, 9] sum is ", get_bst_sum_from_range(p, node1))
