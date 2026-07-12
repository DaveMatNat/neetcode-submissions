class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'}':'{',
                ')':'(',
                ']':'['}
        
        for c in s:
            # if close
            if c in match:
                if stack and stack[-1] == match[c]:
                    stack.pop()
                else:
                    return False
            # if open
            else:
                stack.append(c)

        return True if not stack else False

