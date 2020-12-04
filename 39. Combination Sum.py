class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
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
            self.search(candidates[i:], target - candidates[i], comb + [candidates[i]], result)