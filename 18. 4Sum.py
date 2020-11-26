class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def twoSum(nums, target):
            res = []
            left = 0
            right = len(nums) - 1
            
            while left < right:
                s = nums[left] + nums[right]
                
                if s < target:
                    left += 1
                
                elif s > target:
                    right -= 1
                
                else:
                    res.append([nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
            
            return res
        
        def kSum(nums, target, k):
            res = []
            
            if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
                return res
            
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                    
                for _, num in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                    res.append([nums[i]] + num)  
                
            return res
        
        nums.sort()
        return kSum(nums, target, 4)