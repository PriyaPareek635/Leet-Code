class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid_idx = (left + right) // 2
            if nums[mid_idx] == target:
                return mid_idx
            if nums[mid_idx] < target:
                left = mid_idx + 1
            else:
                right = mid_idx - 1
        
        return left
