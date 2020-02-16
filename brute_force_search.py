T = int(input())


for test_case in range(1, T + 1):
    price = list(map(int, input().split()))
    day_of_month = [0] + list(map(int, input().split()))
    #print(price)
    #print(day_of_month)
    minMonth = [0] * 13
    d = [0] * 13
     
     for i in range(1, 13):
        minMonth[i] = min(price[0] * day_of_month[i], price[1])
    #print(minMonth)
        
     for i in range(1, 13):
        d[i] = d[i-1] + minMonth[i]
        #print("Month " + str(i) + " 누적금액은 " + str(d[i]))
         if i - 3 >= 0:
             if d[i] > d[i-3] + price[2]:
                d[i] = d[i-3] + price[2]
    #print("총 누적금액은 ")
    #print(d)
     
     if d[12] > price[3]:
        d[12] = price[3]
         
     print("#" + str(test_case) + " " + str(d[12]))
