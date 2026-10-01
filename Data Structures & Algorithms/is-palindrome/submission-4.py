class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_s = "".join(char for char in s if char.isalnum())
        front = 0
        back = len(cleaned_s) - 1

        while front < back:

            if cleaned_s[front].lower() != cleaned_s[back].lower():
                return False
            front += 1
            back -= 1

        return True