def phoneCall(min1, min2_10, min11, s):
    if s<min1:
        return 0
    elif s>=min1 and s<=min1+9*min2_10:
        return 1+(s-min1)//min2_10
    return 10 + (s-min1-9*min2_10)//min11


phoneCall(3, 1, 2, 20)
