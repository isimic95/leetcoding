from itertools import accumulate


def sumInRange(nums, queries):
    result = 0
    acc = list(accumulate([0] + nums))

    for i, j in queries:
        result += acc[j+1] - acc[i]

    return result % 1000000007


print(sumInRange([3, 0, -2, 6, -3, 2], [[0, 2], [2, 5], [0, 5]]))
