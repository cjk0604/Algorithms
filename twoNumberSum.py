def twoNumberSum(array, targetSum):
    sum_table = {}
    for num in array:
		potential_num = targetSum - num
		if potential_num in sum_table:
			return [num, potential_num]
		else:
			sum_table[num] = True
	return []
