class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        comb = []
        def backtrack(i):
            if i == len(digits):
                res.append("".join(comb))
                return 
            for char in digitToChar[digits[i]]: 
                comb.append(char)
                backtrack(i+1)
                comb.pop()
        backtrack(0)
        return res

        