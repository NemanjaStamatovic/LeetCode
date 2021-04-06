class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack_out = []
        stack_in = path.split("/")
        
        for item in stack_in:
            
            if item == "" or item == ".":
                continue
                
            if item == "..":
                if stack_out:
                    stack_out.pop(-1)
                
            else:
                stack_out.append(item)
                
        result = "/".join(stack_out)    
        
        return "/" + result