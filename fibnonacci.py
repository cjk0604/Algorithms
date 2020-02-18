def fiboRecursive(num):
    if num <= 1:
        return num
    
    else:
        return fiboRecursive(num-1) + fiboRecursive(num-2)


def fibo_dp(num):
    fibo_result = [0 for i in range(num+1)]
    fibo_result[0] = 0
    fibo_result[1] = 1

    for index in range(2, num+1):
        fibo_result[index] = fibo_result[index-1] + fibo_result[index-2]
    print(fibo_result)
    return fibo_result[num]
print(fibo_dp(10))

