import math

def secondLargest(arr):
    if len(arr) < 2:
        return "NA"

    first = second = -math.inf

    for ele in arr:
        if first > ele:
            first = ele
            second = first

        elif first < ele and ele > second:
            second = ele

    return second

arr = [2,14,1,6,21,9,6 ]

print(secondLargest(arr))
