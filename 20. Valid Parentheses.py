class Solution:
    def isValid(self, s: str) -> bool:
        
        opened = ["(", "[", "{"]
        closed = [")", "]", "}"]
        last = []
        
        for bracket in s:
            if bracket in opened:
                last.append(bracket)
            
            if bracket in closed:
                if len(last) == 0:
                    return False
                if last.pop() != opened[closed.index(bracket)]:
                    return False
                    
        if last:
            return False
        
        return True    