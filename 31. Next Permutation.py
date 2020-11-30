class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        def reverse(nums, i):
            j = len(nums) - 1
            
            while i < j:
                swap(nums, i, j)
                i += 1
                j -= 1
                
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
            
        if i > 0:
            j = len(nums) - 1
            
            while j > i and nums[j] <= nums[i - 1]:
                j -= 1
                
            swap(nums, i - 1, j)
            
        reverse(nums, i)    
    
#         nums_sorted = sorted(nums)
#         nums_sorted = permutations(nums_sorted)
#         nums_sorted = [p for p in nums_sorted]
        
#         nums_sorted1 = []
#         for i in range(len(nums_sorted)):
#             if nums_sorted[i] not in nums_sorted1:
#                 nums_sorted1.append(nums_sorted[i])
        
#         for i in range(len(nums_sorted1)):
#             if list(nums_sorted1[i]) == nums:
#                 if i < len(nums_sorted1) - 1:
#                     for j in range(len(nums)):
#                         nums[j] = nums_sorted1[i + 1][j]
#                 else:
#                     for j in range(len(nums)):
#                         nums[j] = nums_sorted1[0][j]
#                 break
                
        
                
                
