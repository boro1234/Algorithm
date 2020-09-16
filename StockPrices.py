# Given an array of stock prices, design an algorithm to find the maximum profit after at one most one buy and one sell. 
# You cannot sell a stock before you buy one.

def maxProfits(prices):
    if len(prices) <= 1:
        return 0
    temp = prices[0]
    result = 0
    for price in prices:
        temp = min(price,temp)
        result = max(result,price-temp)
    return result


print(maxProfits([3,2,1]))        #0
print(maxProfits([1,5,7,2]))     #6
print(maxProfits([3,6,2,9]))     #7
print(maxProfits([3,6,2,3]))     #3
print(maxProfits([]))            #0
print(maxProfits([1,1,1,1,1,1])) #0
