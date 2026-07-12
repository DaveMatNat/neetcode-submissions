class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []
        for t in tokens:
            if t not in operators: # a number
                stack.append(t)
            else:
                back,front = stack.pop(), stack.pop()
                if t == "/":
                    stack.append(str(int(int(front)/int(back))))
                else:
                    stack.append(str(int(eval(f"{front}{t}{back}"))))
            
        return int(stack[-1])