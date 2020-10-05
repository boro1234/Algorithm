# -*- coding: utf-8 -*-
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s. 
# If there isn't one, return 0 instead.

# Input: s = 7, nums = [2,3,1,2,4,3] => Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

# I'm still working on it

def minimumSubArraySum(nums,s):
    l1 = []
    l2 = []
    for i,n in enumerate(nums):
        if(i == 0):
            l1.append(n)
            print(l1)
            continue
        if(i != 0 and(nums[i-1]==n-1 or nums[i-1]==n+1)):
            l1.append(n)
            print("if1")
            print(l1)
            continue
        else:
            if(sum(l1) >= s and len(l1) < len(l2)):
                print("if2")
                print(l1)
                l2 = l1
                print(l2)
            else:
                l1 = []
                l1.append(n)
                print("end")
    return len(l2)

print(minimumSubArraySum([2,3,1,2,4,3],7))





 