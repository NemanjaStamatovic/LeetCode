class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        
        for word in strs:
            key = "".join(sorted(word))
            
            if key in result:
                result[key].append(word)
                
            else:
                result[key] = [word]
                
        return list(result.values())        
        
        
        
        
        
#         result = []
        
#         for word in strs:
            
#             b = False
#             for i in range(len(result)):
#                 if sorted(word) == sorted(result[i][0]):
#                     result[i].append(word)
#                     b = True
#                     break
            
#             if b == False:
#                 result.append([word])
            
#         return result    