class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
                break
                
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                result.append(i)
                break
        
        if result:
            return result
        
        return [-1, -1]        