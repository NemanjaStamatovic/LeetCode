class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target not in nums:
            return -1
        
        for i, e in enumerate(nums):
            if e == target:
                return i
                