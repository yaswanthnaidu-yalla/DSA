class Solution:
    def productExceptSelf(self, nums):
        result=[1]*len(nums)
        running=1
        for i in range (0,len(nums),1):
            result[i]=running
            running = running*nums[i] 
        running=1 
        for i in range (len(nums)-1,-1,-1):
            result[i]*= running
            running*=nums[i]
            
            
        
        return result



            

        