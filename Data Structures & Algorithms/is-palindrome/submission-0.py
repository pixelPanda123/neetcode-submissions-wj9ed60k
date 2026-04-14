class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new = "".join(x.lower() for x in s if x.isalnum())
        return new ==new[::-1]
        