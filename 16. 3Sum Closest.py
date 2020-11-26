class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        result = [nums[0], nums[1], nums[2]]
        closest = abs(target - sum(result))
        
        for first in range(len(nums)-2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
                
            left = first + 1
            right = len(nums) - 1

            while left < right:
                s = nums[first] + nums[left] + nums[right]
                if abs(s - target) < closest:
                    closest = abs(s - target)
                    result = [nums[first], nums[left], nums[right]]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return target
                
        return sum(result)        