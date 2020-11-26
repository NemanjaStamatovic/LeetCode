class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(s="", left=0, right=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            
            if left < n:
                backtrack(s+"(", left+1, right)
                
            if right < left:
                backtrack(s+")", left, right+1)
                
        result = []
        backtrack()
        
        return result
        
#         parentheses = "()" * n
#         parentheses = set(permutations(parentheses))
#         parentheses = ["".join(parenthese) for parenthese in parentheses]
        
#         result = set()
#         for parenthese in parentheses:
#             if self.isValid(parenthese):
#                 result.add(parenthese)
        
#         return result
    
#     def isValid(self, s: str) -> bool:
        
#         stack = []
#         parentheses = {")": "(", "]": "[", "}": "{"}
        
#         for p in s:
#             if p in parentheses:
#                 if len(stack) == 0:
#                     return False
#                 if stack.pop() != parentheses[p]:
#                     return False
#             else:
#                 stack.append(p)
                
#         if stack:
#             return False
#         return True