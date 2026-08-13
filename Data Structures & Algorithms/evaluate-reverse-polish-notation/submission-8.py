class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        eval_int = 0

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))

            else:
                if tokens[i] == "+":
                    last, second_last = stack.pop(), stack.pop()
                    stack.append(last + second_last)
                elif tokens[i] == "-":
                    last, second_last = stack.pop(), stack.pop()
                    stack.append(second_last - last)
                elif tokens[i] == "*":
                    last, second_last = stack.pop(), stack.pop()
                    stack.append(last * second_last)
                else:
                    last, second_last = stack.pop(), stack.pop()
                    stack.append(int(second_last / last))

        return stack[-1]