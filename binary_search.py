def binarySearch(data, target):
    print(data)
    if len(data) == 1 and target == data[0]:
        return True
    elif len(data) == 1 and target != data[0]:
        return False
    elif len(data) == 0:
        return False

    medium = len(data) // 2
    if data[medium] == target:
        return True
    else:
        if data[medium] < target:
            return binarySearch(data[medium:], target)
        else:
            return binarySearch(data[:medium], target)

data=[1,2,3,4,5,6,7,8]
print(binarySearch(data, 6))
print("=============")
print(binarySearch(data, 9))
