class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_braces = "({["

        for char in s:
            if char in opening_braces:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ")" and stack[-1] != "(":
                    return False
                elif char == "}" and stack[-1] != "{":
                    return False
                elif char == "]" and stack[-1] != "[":
                    return False
                else:
                    stack.pop(len(stack)-1)

        return True if len(stack) == 0 else False