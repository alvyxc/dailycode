#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
#and deserialize(s), which deserializes the string back into the tree.

class Node:
    left = None
    right = None
    val = None

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():

    t3 = Node("t3")
    t4 = Node("t4")

    t5 = Node("t5")
    t6 = Node("t6")

    t1 = Node("t1", None, t4)
    t2 = Node("t2", t5, None)

    return Node("t0", t1, t2)


def in_order_serial_tree(t):

    if t is None:
        return "X"

    return t.val + "," + in_order_serial_tree(t.left) + "," + in_order_serial_tree(t.right)


def deserialize_tree(data_list):

    if data_list[0] == 'X':
        return None

    d_tree = Node(data_list[0])
    data_list.pop(0)
    d_tree.left = deserialize_tree(data_list)
    data_list.pop(0)
    d_tree.right = deserialize_tree(data_list)
    return d_tree

tree = build_tree()

serialized_data = in_order_serial_tree(tree)
print(serialized_data)

data_list = str.split(serialized_data, ",")

d_tree = deserialize_tree(data_list)

serialized_data_2 = in_order_serial_tree(d_tree)

print(serialized_data_2)