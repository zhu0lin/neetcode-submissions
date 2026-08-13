class Solution:
    def isValid(self, s: str) -> bool:
        """
        U: 
        Input: A string s consisting of '(', ')', '{', '}', '[' and ']'.
        P:
        Stack approach:
        If char is open brace, add it to the stack
        If char is closing brace, check what type of closing brace it 
        is. Check if the char on the top of the stack is the matching 
        opening brace. If it is, pop it off the top of the stack. If 
        it is not, return false immediately.

        Return true at the end
        """
        stack = []
        opening = "({["
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ")":
                    if stack[-1] != "(":
                        return False
                elif char == "}":
                    if stack[-1] != "{":
                        return False
                else:
                    if stack[-1] != "[":
                        return False
                stack.pop()

        return True if len(stack) == 0 else False