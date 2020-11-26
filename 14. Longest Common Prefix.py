class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        strs.sort()
        result = ""
        
        for i, j in zip(strs[0], strs[-1]):
            if i == j:
                result += i
            else:
                break
                
        return result        
        
#         if len(strs) == 0:
#             return ""
        
#         result = ""
#         min_str = strs[0]
        
#         for i in range(1, len(strs)):
#             if len(strs[i]) < len(min_str):
#                 min_str = strs[i]
                
#         for i in range(len(min_str)):
#             b = True
#             for j in range(len(strs)):
#                 if strs[j][i] != min_str[i]:
#                     b = False
#                     break
#             if b:
#                 result += min_str[i]
#             else:
#                 break
        
#         return result