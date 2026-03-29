class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for par in s:
            if par in pairs:
                if not stack or stack[-1] != pairs[par]:
                    return False
                stack.pop()
            else:
                stack.append(par)

        return not stack 
        

