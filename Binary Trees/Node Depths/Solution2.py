# iterative approach using a stack approach
# also O(N) time and O(h) space
def nodeDepths(root):
	sumOfDepths = 0
    # Write your code here.
	stack = [{"node": root, "depth": 0}]
    # while stack is not empty of nodes to sum depth of
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo["node"], nodeInfo["depth"]
		if node is not None:
			sumOfDepths += depth
			stack.append({"node": node.left, "depth": depth + 1})
			stack.append({"node": node.right, "depth": depth + 1})

	return sumOfDepths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
