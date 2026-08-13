class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Understand:
        Input: An array of strings, which are either integers
        or operators

        Plan:
        Stack approach

        Iterate over tokens
        If the string is an integer, push it onto the stack
        Else the string must be an operator. In this case, 
        iterate over the stack until it is empty. Perform the operation
        on the numbers that were popped from the stack.

        Keep track of the resulting integer after the operation.
        Repeat.
        """
        s = []
        res = 0
        for token in tokens:
            if token == "+":
                top = s.pop()
                bottom = s.pop()
                s.append(top + bottom)
            elif token == "-":
                top = s.pop()
                bottom = s.pop()
                s.append(bottom - top)
            elif token == "*":
                top = s.pop()
                bottom = s.pop()
                s.append(top * bottom)
            elif token == "/":
                top = s.pop()
                bottom = s.pop()
                s.append(int(bottom/top))
            else:
                s.append(int(token))
            
                

        return int(s[-1])
