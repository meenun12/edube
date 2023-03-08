"""
Given a root node of the input binary tree:
Node contain three elements:
   int value;
   Node Left; # pointer left child
   Node Right # pointer of right

-------question 1----------
if_the_path_for_target_exists(Node root, int target): boolean

------question 2------------
get_the_path(Node root, target):List[Node]
"""

from typing import List

class Node:
    def __init__(self, value: int, Left: 'Node' = None, Right: 'Node' = None):
        self.value = value
        self.Left = Left
        self.Right = Right

def if_the_path_for_target_exists(root: Node, target: int) -> bool:

    if root is None:
        return False

    if root.value == target:
        return True

    return if_the_path_for_target_exists(root.Left, target) or if_the_path_for_target_exists(root.Right, target)

def get_the_path(root: Node, target: int) -> List[Node]:

    if root is None:
        return []

    if root.value == target:
        return [root]

    left_path = get_the_path(root.Left, target)
    right_path = get_the_path(root.Right, target)

    if left_path:
        left_path.append(root)
        return left_path

    if right_path:
        right_path.append(root)
        return right_path

    return []

    # If target is found in right subtree, add current node to path and return
    if right_path:
        right_path.append(root)
        return right_path

    # If target is not found in either subtree, return an empty path
    return []

# Create a binary tree with Node objects
root = Node(1)
root.Left = Node(2)
root.Right = Node(3)
root.Left.Left = Node(4)
root.Left.Right = Node(5)
root.Right.Left = Node(6)
root.Right.Right = Node(7)

# Call the if_the_path_for_target_exists method to check if a target node exists in the tree
if if_the_path_for_target_exists(root, 5):
    print("Target node exists in the tree")
else:
    print("Target node does not exist in the tree")

# Call the get_the_path method to get the path to a target node in the tree
path = get_the_path(root, 5)
if path:
    print("Path to target node:", [node.value for node in path])
else:
    print("Target node does not exist in the tree")

