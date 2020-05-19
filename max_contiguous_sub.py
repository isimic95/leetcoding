def arrayMaxConsecutiveSum2(inputArray):
    if not nums:
        return 0

    maxx = -2147483648
    current = 0
    
    for x in nums:
        if current < 0:
            current = x
        else:
            current += x
        maxx = max(maxx, current)
            
    return maxx
