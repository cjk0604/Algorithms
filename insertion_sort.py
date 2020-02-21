def insertionSort(data):
    for index in range(len(data)):
        stand = data[index]
        for index2 in range(index, 0, -1):
            if stand < data[index2-1]:
                data[index2], data[index2 -1] = data[index2-1], data[index2]
            else:
                break
    return data



data=[3,1,2]
print(insertionSort(data))