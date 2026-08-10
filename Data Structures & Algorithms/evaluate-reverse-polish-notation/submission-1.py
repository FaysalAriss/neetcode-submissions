class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        leftOperand, rightOperand = 0,0 #assumes first two tokens are numbers/valid sequence
        for token in tokens:
            if token in operators:
                rightOperand = stack.pop()
                leftOperand = stack.pop()

            if token == "+":
                stack.append(leftOperand + rightOperand)
            elif token == "-":
                stack.append(leftOperand - rightOperand)
            elif token == "*":
                stack.append(leftOperand * rightOperand)
            elif token == "/":
                stack.append(int(leftOperand / rightOperand)) #truncate towards 0
            else:
                stack.append(int(token))

        return stack.pop()