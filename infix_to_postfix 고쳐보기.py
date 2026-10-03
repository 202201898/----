def precedence(self, op):
    if op in('+', '-'):
        return 1
    elif op in ('*','/'):
        return 2
    elif op == '^':
        return 3
    return 0

def infix_to_postfix(self, expression):
    
    self.stack = [] # Reset stack
    self.output = [] # Reset output

    expression = self.tokenization(expression)
    for token in expression:
        if self.is_operand(token):
            self.output.append(token)
        elif token == '(':
            self.stack.append(token)
        elif token == ')':
            while self.stack and self.stack[-1] != '(':
                self.output.append(self.stack.pop())
            self.stack.pop() # pop '('
        else: # Operator
            while self.stack and self.precedence(self.stack[-1]) >= self.precedence(token):
                if token == '^' and self.stack[-1] == '^':  #거듭제곱이 연속으로 나올때는 pop하지 않음
                    break

                self.output.append(self.stack.pop())
            self.stack.append(token)
    while self.stack:
        self.output.append(self.stack.pop())
    return ' '.join(self.output)