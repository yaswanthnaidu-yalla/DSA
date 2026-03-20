class Solution:
    def maxSubArray(self, nums) -> int:
        current=nums[0]
        maxSum=nums[0]
        for i in range(1,len(nums)):
            current=(max(current+nums[i], nums[i]))
            if current>maxSum:
                maxSum=current
        return maxSum

            
