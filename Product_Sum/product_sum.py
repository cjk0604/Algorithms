def productSum(array, degree=1):
    sum = 0
    for number in array:
        if type(number) is list:
            sum += productSum(number, degree + 1)
        else:
            sum += number
    return sum * degree