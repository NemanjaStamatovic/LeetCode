class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.sort()
        
        if not nums:
            return 1
        
        if len(nums) == 1:
            if nums[0] != 1:
                return 1
            return 2
        
        if nums[0] > 1:
            return 1
        
        if nums[-1] <= 0:
            return 1
        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1 and nums[i + 1] > 1:
                if nums[i] <= 0:
                    return 1
                
                return nums[i] + 1
            
        return nums[-1] + 1    