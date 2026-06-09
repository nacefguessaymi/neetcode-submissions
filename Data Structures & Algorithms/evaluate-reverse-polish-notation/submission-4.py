class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            try:
                num = int(tok)
                stack.append(num)
            except ValueError:
                if tok == "+":
                    j = stack.pop()
                    i = stack.pop()
                    stack.append(i + j)
                elif tok == "-":
                    j = stack.pop()
                    i = stack.pop()
                    stack.append(i - j)
                elif tok == "*":
                    j = stack.pop()
                    i = stack.pop()
                    stack.append(i * j)
                elif tok == "/":
                    j = stack.pop()
                    i = stack.pop()
                    stack.append(int(i / j))
        return stack[0]