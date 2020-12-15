class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        start_position = 0
        end_position = nums[start_position]
        jumps = 1
        
        while end_position < len(nums) - 1:
            
            jumps += 1
            temp = end_position
            
            for i in range(start_position + 1, end_position + 1):
                if i + nums[i] > temp:
                    temp = i + nums[i]
           
            start_position = end_position
            end_position = temp
            
        return jumps    