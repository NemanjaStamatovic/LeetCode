from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_count = Counter(words)
        result = []
        
        for i in range(len(s) - len(words) * len(words[0]) + 1):
            used_words = 0
            checked_words = dict(word_count)
            
            for j in range(i, i + len(words) * len(words[0]), len(words[0])):
                if s[j:j + len(words[0])] in checked_words and checked_words[s[j:j + len(words[0])]] > 0:
                    used_words += 1
                    checked_words[s[j:j + len(words[0])]] -= 1
                else:
                    break
                    
            if used_words == len(words):
                result.append(i)
                
        return result        
        
#         perm = permutations(words)
#         perm = ["".join(p) for p in perm]
#         perm = set(perm)
        
#         res = []
        
#         for p in perm:
#             matches = re.finditer(p, s)
#             matches_positions = [match.start() for match in matches]
#             if matches_positions:
#                 for m in matches_positions:
#                     res.append(m)     
        
#         return res       