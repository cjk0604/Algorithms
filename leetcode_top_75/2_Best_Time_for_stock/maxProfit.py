def maxProfit(nums):
    min_price = float("inf")
    max_profit = 0

    for price in nums:
        if price < min_price:
            min_price = price
        else:
            if max_profit < price - min_price:
                max_profit = price - min_price
    return max_profit
    

# Given Input: [7,1,5,3,6,4]

# Output: 5


data = [7, 1, 5, 3, 6, 4]
#output = 5
print(maxProfit(data))

