def longestValidParentheses(s):
    stack = [-1]
    maxlen = 0
    for i in range(len(s)):
        if (s[i] == "("):
            stack.append(i)
        else:
            stack.pop()
            if (len(stack) == 0):
                stack.append(i)
            else:
                maxlen = max(maxlen, i - stack[-1])
    return maxlen
s=")()())"
print(longestValidParentheses(s))