class Solution(object):
    def searchRange(self, nums, target):
        y=nums.count(target)
        if y==0:
            return[-1,-1]
        return[nums.index(target),nums.index(target)+y-1]
        
