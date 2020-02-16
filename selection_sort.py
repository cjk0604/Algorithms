def selectionSort(data):
    for stand in range(len(data) - 1):
        min = stand
        for index in range(stand+1, len(data)):
            if data[min] > data[index]:
                min = index
        data[stand], data[min] = data[min], data[stand]
    return data


data = [8,7,6,5,2,4,0]
print(selectionSort(data))