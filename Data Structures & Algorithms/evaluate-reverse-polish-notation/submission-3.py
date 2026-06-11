class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0: 
            return -1 
        if len(tokens) == 1: 
            return int(tokens[0])
        operators = ['+', '-', '*','/']
        stack = []


        for x in range(len(tokens)): 
            if tokens[x] not in operators: 
                stack.append(tokens[x])
            else: 
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                operator = tokens[x]
                if operator == "+":
                    res = op2 + op1 
                elif operator == "*":
                    res = op2 * op1 
                elif operator == "-":
                    res = op2-op1
                else: 
                    res = op2/op1 
                 
                stack.append(res)
        return int(stack[-1])


        