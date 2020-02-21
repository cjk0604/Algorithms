def binarySearch(data, target):
    print(data)
    if len(data) == 1 and target == data[0]:
        return 0
    elif len(data) == 1 and target != data[0]:
        return -1
    elif len(data) == 0:
        return -1

    medium = len(data) // 2
    if data[medium] == target:
        return medium
    else:
        if data[medium] < target:
            return binarySearch(data[medium:], target)
        else:
            return binarySearch(data[:medium], target)



# AlgoExpert
def binarySearch_Algoexpert(array, target):
    return binarySearchHelper_Algoexpert(array, target, 0, len(array)-1)

def binarySearchHelper_Algoexpert(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) //2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper_Algoexpert(array, target, left, middle-1)
    else:
        return binarySearchHelper_Algoexpert(array, target, middle+1, right)

def binarySearch_optimal_solution(array, target):
    return binarySearch_Helper_optimal_solution(array, target, 0, len(array)-1)


def binarySearch_Helper_optimal_solution(array, target, left, right):
    while left <= right:
        mid = (left + right) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

data=[1,5,7,23,111]
print(binarySearch_optimal_solution(data, 23))
print("=============")
