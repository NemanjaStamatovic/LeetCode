class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] < target:
                left = middle + 1
                
            elif nums[middle] > target:
                right = middle - 1
                
            else:
                return middle
            
        return left
        
#         if target < nums[0]:
#             return 0
        
#         for i in range(len(nums) - 1):
#             if nums[i] == target:
#                 return i
            
#             if nums[i] < target and nums[i + 1] > target:
#                 return i + 1
            
#         if nums[-1] == target:
#             return len(nums) - 1
        
#         if nums[-1] < target:
#             return len(nums)