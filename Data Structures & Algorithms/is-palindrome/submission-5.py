class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        letters = "".join([char for char in s if char.isalnum()])
        letters_only = letters.lower()
        left = 0
        right = len(letters_only)-1
        while right>left:
            if (letters_only[left] != letters_only[right]) or len(letters_only)<=1:
                return False
        
            right-=1
            left+=1
        return True