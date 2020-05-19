# Solution 1
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    memo = []
    memo.append(1)
    memo.append(2)

    for i in range(2, n):
        memo.append(0)
        memo[i] = memo[i-1] + memo[i-2]

    return memo.pop()


# Solution 2
def climbStairs2(self, n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    n_1, n_2 = 1, 2

    for i in range(2, n):
        n_1, n_2 = n_1+n_2, n_1

    return n_1
