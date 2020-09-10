## Two Sum: Given an array of integers, return indices of two numbers that add up to the target.
## For example, nums = [2,5,1,4] & target = 9 -> Expected output is [1,3]

def twoSum(nums, target):
  d = {}                         # dict for diff. 
  for i, v in enumerate(nums):
      diff = target - v          # diff between target and value of nums
      if diff in d:
          return [d[diff], i]
      else:
          d[v] = i               
  return [-1,-1]                 # There is no number add up to the target

nums = [2,5,1,4]
target = 9
print (twoSum(nums,target)) #[1,3]

nums = [3,1,8,2,5]
target = 7
print (twoSum(nums,target)) #[3.4]

nums = [1]
target = 7
print (twoSum(nums,target)) #[-1,-1]

