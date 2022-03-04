def scoreOfParentheses(s):
    stack = []
    for i in s:
        if (i == "("):
            stack.append(i)
        else:
            if (stack[-1] == "("):
                stack.pop()
                stack.append(1)
            else:
                sum = 0
                while (stack[-1] != "("):
                    sum += stack.pop()
                stack.pop()
                stack.append(2 * sum)
    x=sum(stack)
    return x

s="(()(()))"
print(scoreOfParentheses(s))