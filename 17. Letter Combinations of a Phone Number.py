class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        if len(digits) == 0:
            return []
        
        result = [""]
        
        for digit in digits:
            result = [res + current for res in result for current in phone[digit]]
            
        return result    
       
        
        
        # all_combinations = [''] if digits else []
        # for digit in digits:
        #     current_combinations = list()
        #     for letter in interpret_digit[digit]:
        #         for combination in all_combinations:
        #             current_combinations.append(combination + letter)
        #     all_combinations = current_combinations
        # return all_combinations