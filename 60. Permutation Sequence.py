from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        l = [str(num) for num in range(1, n+1)]
        
        perm = permutations(l)
        
        perm_k = list(perm)[k-1]
        result = ""
        for i in perm_k:
            result += i
        
        return result