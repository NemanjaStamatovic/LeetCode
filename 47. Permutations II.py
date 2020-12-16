class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums = permutations(nums)
        nums = set(nums)
        
        return nums