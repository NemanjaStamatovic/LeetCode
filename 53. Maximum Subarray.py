class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)
        
#         result = nums[0]
        
#         for i in range(len(nums)):
#             temp = nums[i]
#             if temp > result:
#                 result = temp
#             for j in range(i + 1, len(nums)):
#                 temp += nums[j]
#                 if temp > result:
#                     result = temp
                    
#         return result            