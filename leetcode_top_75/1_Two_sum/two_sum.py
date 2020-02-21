def two_sum(nums, target):
    sum_list = {}
    
    for index in range(len(nums)):
        potential_sum = target - nums[index]
        if potential_sum in sum_list:
            return [sum_list[potential_sum], index]
        else:
            sum_list[nums[index]] = index
    return []


# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].


data = [2, 7, 11, 15]
target = 9
print(two_sum(data, target))

