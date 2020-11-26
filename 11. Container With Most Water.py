class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        result = 0
        
        left = 0
        right = len(height) - 1
        
        while left < right:
            result = max(result, min(height[left], height[right])*(right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return result        
        
#         while len(height) >= 2:
#             temp = (len(height) - 1) * min(height[0], height[-1])
#             if temp > result:
#                 result = temp
#             if height[0] == min(height[0], height[-1]):
#                 height = height[1:]
#             else:
#                 height = height[:len(height)-1]
                
#         return result        