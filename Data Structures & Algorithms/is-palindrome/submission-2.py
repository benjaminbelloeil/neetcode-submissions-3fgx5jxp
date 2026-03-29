class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''

        for char in s:
            if char.isalnum():
                string += char.lower()
        
        if string[::-1] == string:
            return True
        else:
            return False