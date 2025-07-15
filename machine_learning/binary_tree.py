# Define a Node of the binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Define the Binary Tree
class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    # Example method: insert a node (manual, not BST-style)
    def insert_left(self, current_node, value):
        current_node.left = Node(value)
        return current_node.left

    def insert_right(self, current_node, value):
        current_node.right = Node(value)
        return current_node.right

    # Example method: In-order Traversal (Left -> Root -> Right)
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)


# Create the tree
tree = BinaryTree(1)

# Add nodes
left_child = tree.insert_left(tree.root, 2)
right_child = tree.insert_right(tree.root, 3)
tree.insert_left(left_child, 4)
tree.insert_right(left_child, 5)

print("In-order traversal:")
tree.inorder_traversal(tree.root)