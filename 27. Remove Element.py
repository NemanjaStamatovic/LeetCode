class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        head = 0
        curr = 0
        
        while curr < len(nums):
            if nums[curr] == val:
                curr += 1
            else:
                nums[head] = nums[curr]
                head += 1
                curr += 1
            
        return head  