class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if sum(candidates) < target:
            return []
        
        candidates.sort()
        result = []
        
        self.search(candidates, target, [], result)
        
        return result
    
    def search(self, candidates, target, comb, result):

        if target < 0:
            return
        
        if target == 0:
            result.append(comb)
            return
        
        for i in range(len(candidates)):
            if comb + [candidates[i]] not in result:
                self.search(candidates[i + 1:], target - candidates[i], comb + [candidates[i]], result)