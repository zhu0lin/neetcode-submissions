class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        formatted_str = ''.join(char for char in s if char.isalnum())
        left = 0
        right = len(formatted_str)-1

        while left < right:
            if formatted_str[left].lower() != formatted_str[right].lower():
                return False
            left += 1
            right -= 1

        return True