#You are a professional robber planning to rob houses along a street. 
#Each house has a certain amount of money stashed, 
#the only constraint stopping you from robbing each of them is 
#that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

def houserobbber(nums):
    prevMax = 0                             
    currMax = 0
    for num in nums:
        temp = currMax                     
        currMax = max(prevMax+num,currMax)  #this means comparison previous addition with current
        prevMax = temp
    return currMax

# if two doors away also has security system connected (my question)
def houserobber2(nums):
    prevMax1 = 0
    prevMax2 = 0
    currMax = 0
    for num in nums:
        temp1 = prevMax2
        temp2 = currMax
        currMax = max(prevMax1+num,prevMax2,currMax)
        prevMax1 = temp1
        prevMax2 = temp2
    return currMax


print(houserobbber([2,7,8,9,4,5])) #21
print(houserobbber([2,11,8,4,9])) #20
print(houserobbber([3])) #3
print(houserobbber([1,1,1,1,1,1])) #3

print(houserobber2([2,7,8,9,4,5])) #13
print(houserobbber([2,11,8,4,9])) #20
print(houserobber2([2,7,8,9,4,5,6,9,2,3])) 


