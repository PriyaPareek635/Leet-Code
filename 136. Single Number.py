class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            c=nums.count(i)
            if c==1:
                return i
