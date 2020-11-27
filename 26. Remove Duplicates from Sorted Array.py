class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        head = 0
        curr = 0
        
        while curr < len(nums) - 1:
            
            if nums[curr] == nums[curr + 1]:
                curr += 1
                
            else:
                nums[head + 1] = nums[curr + 1]
                head += 1
                curr += 1
                
        return head + 1    