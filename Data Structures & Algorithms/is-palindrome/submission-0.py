class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        left = 0
        right = len(s)-1
        while (left < right):
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True