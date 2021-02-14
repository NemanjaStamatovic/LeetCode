class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            if len(merged) == 0:
                merged.append(interval)
            
            elif merged[-1][1] < interval[0]:
                merged.append(interval)
                
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged