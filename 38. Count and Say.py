class Solution:
    def countAndSay(self, n: int) -> str:
        
        def say(s):
            stack = ""
            result = ""

            for i in range(len(s)):
                if stack:

                    if stack == s[i]:
                        count += 1

                    else:
                        result += str(count)
                        result += stack
                        stack = s[i]
                        count = 1 

                else:
                    stack = s[i]
                    count = 1

            result += str(count)
            result += stack         

            return result
        
        res = "1"
        for i in range(2, n + 1):
            res = say(res)
        
        return res