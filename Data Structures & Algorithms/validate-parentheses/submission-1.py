class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftParenthesis = ['(', '[', '{']
        rightParenthesis = [')', ']', '}']
        for char in s:
            if char in rightParenthesis:
                if len(stack) == 0 or not leftParenthesis.index(stack.pop()) == rightParenthesis.index(char):
                    return False
            else:
                stack.append(char)

        return len(stack) == 0