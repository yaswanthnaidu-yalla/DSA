class Solution:
   def containsDuplicate(self, nums):
    seen = {}
    for i in range (len(nums)):
        need = nums[i]
        if need in seen:
            return print("true")
        else:
            return print("false")  
    seen[nums[i]]=i 