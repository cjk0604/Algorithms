def merge(left, right):
    merged = list()
    left_pt, right_pt = 0, 0

    while len(left) > left_pt and len(right) > right_pt:
        if left[left_pt] < right[right_pt]:
            merged.append(left[left_pt])
            left_pt += 1
        else:
            merged.append(right[right_pt])
            right_pt += 1

    while len(left) > left_pt:
        merged.append(left[left_pt])
        left_pt += 1

    while len(right) > right_pt:
        merged.append(right[right_pt])
        right_pt += 1

    return merged


def mergeSplit(data):
    if len(data) <= 1:
        return data
    
    medium = int(len(data) / 2)
    left = mergeSplit(data[:medium])
    right = mergeSplit(data[medium:])
    return merge(left, right)


data = [9, 8, 7, 3, 5, 4, 2, 1, 0]
print(data)

print(mergeSplit(data))
