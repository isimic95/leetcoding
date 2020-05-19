def romanToInt(s: str) -> int:
    mapper = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    sum = 0
    z = float('inf')
    prev = 0

    for c in s:
        value = mapper[c]

        if value < z:
            sum += value
            prev = value
            z = value
        else:
            sum += value - prev*2
    return sum


print(romanToInt("III"))
