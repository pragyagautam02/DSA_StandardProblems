def largestRectangleArea(heights):
    left = []
    right = []
    stack1 = []
    stack2 = []
    n = len(heights)

    for i in range(n):
        while (len(stack1) != 0 and stack1[-1][0] >= heights[i]):
            stack1.pop()
        if (len(stack1) == 0):
            left.append(len(heights) + 1)
        else:
            left.append(stack1[-1][1])
        stack1.append([heights[i], i])

    for i in range(n - 1, -1, -1):
        while (len(stack2) != 0 and stack2[-1][0] >= heights[i]):
            stack2.pop()
        if (len(stack2) == 0):
            right.append(len(heights) + 1)
        else:
            right.append(stack2[-1][1])
        stack2.append([heights[i], i])
    print("Left : ",left)
    maxarea = 0
    for i in range(len(left)):
        w = (abs(left[i] - right[i])) - 1
        area = heights[i] * w
        #print(area)
        if (area > maxarea):
            maxarea = area
    print("Right : ",right)
    return maxarea

heights= [1,2,3,4,5]
print(largestRectangleArea(heights))
