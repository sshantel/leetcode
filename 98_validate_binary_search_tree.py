"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
import sys
class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

def validate_bst(root, min= -sys.maxsize, max = sys.maxsize):
    if root == None:
        return True
    if (root.value > min and root.value < max and validate_bst(root.left_child, min, root.value) and 
    validate_bst(root.right_child, root.value,max)):
        return True
    else:
        return False
root = Node(5)
l = Node(4)
r = Node(6)

root.left_child = l
root.right_child = r
print(validate_bst(root))
