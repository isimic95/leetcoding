def isHappy(n):
    digits = []
    i = 0
    result = 0

    while result != 1 and i < 10:
        while n > 0:
            digits.append(n % 10)
            n = n // 10

        result = sum(x**2 for x in digits)
        n = result
        digits = []
        i += 1

    if result == 1:
        return True
    else:
        return False


print(isHappy(2))
