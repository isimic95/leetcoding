def reverse(x: int) -> int:
    s = str(x)
    if x > 2**31 - 1 or x < -2**31:
        return 0

    if x < 0:
        s = s[::-1]
        r = -int(s[:-1])
    else:
        r = int(s[::-1])
    return r


print(reverse(1534236469))
