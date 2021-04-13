class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            v=nums.count(i)
            if v==1:
                return i
                
            
        
        
