class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                if(nums[j] == target - nums[i]):
                    return [i,j]