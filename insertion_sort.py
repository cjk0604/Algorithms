def insertionSort(data):
    for index in range(len(data)):
        stand = data[index]
        for index2 in range(index, 0, -1):
            if stand < data[index2-1]:
                data[index2], data[index2 -1] = data[index2-1], data[index2]
            else:
                break
    return data


data = [8,7,5,3,6,1,9]
print(insertionSort(data))