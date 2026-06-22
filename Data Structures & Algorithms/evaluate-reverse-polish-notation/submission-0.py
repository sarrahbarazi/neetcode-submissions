class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            # If it's not an operator, it's a number
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                # Pop the two numbers to operate on
                right_num = stack.pop()
                left_num = stack.pop()
                
                # Perform the operation based on the token
                if i == "+":
                    stack.append(left_num + right_num)
                elif i == "-":
                    stack.append(left_num - right_num)
                elif i == "*":
                    stack.append(left_num * right_num)
                elif i == "/":
                    stack.append(int(left_num / right_num))
                    
        return stack[0]

        