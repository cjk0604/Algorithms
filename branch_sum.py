def binaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSum(root):
    branch_sum = []
    calculate(root, 0, branch_sum)
    return

def calculateBranchSum(node, running_sum, branch_sum):
    
    if node is None:
        return


    new_running_sum = running_sum + node.value
    if node.left is None and node.right is None:
        branch_sum.append(new_running_sum)
    
    calculateBranchSum(node.left, new_running_sum, branch_sum)
    calculateBranchSum(node.right, new_running_sum, branch_sum)
