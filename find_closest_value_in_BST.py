def findClosestValueInBst(tree, target):
    # Write your code here.
	return findClosestValueInBstHelper(tree, target, float("inf"))


def findClosestValueInBstHelper(tree, target, closest):
	current_node = tree
	while current_node is not None:
		if abs(target - closest) > abs(target - current_node.value):
			closest = current_node.value
		if target < current_node.value:
			current_node = current_node.left
		elif target > current_node.value:
			current_node = current_node.right
		else:
			break

	return closest
