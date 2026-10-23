class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')' : '(', '}' : '{',']' : '['}

        if s == "":
            return True

        for ch in s:
            if ch in pairs:
                if not stack:
                    return False
                else:
                    if stack[-1] != pairs[ch]:
                        return False
                    
                    stack.pop()
            else:
                stack.append(ch)

        return not stack
