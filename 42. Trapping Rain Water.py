class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0
        
        result = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        
        while left < right:
            
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max < right_max:
                result += left_max - height[left]
                left += 1
            else:
                result += right_max - height[right]
                right -= 1
                
        return result        
        
#         result = 0
        
#         for i in range(len(height)):
            
#             left = 0
#             right = 0
            
#             for j in range(i, -1, -1):
#                 left = max(left, height[j])
                
#             for j in range(i, len(height)):
#                 right = max(right, height[j])
                
#             result += min(left, right) - height[i]
            
#         return result    