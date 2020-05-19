def concatenationsSum(a):
    result = 0
    for x in a:
        for y in a:
            result += int("".join([str(x), str(y)]))
    return result
