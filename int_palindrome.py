class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ if x < 0:
            return False

        p = 0
        digits = []

        x_temp = x
        while x_temp > 0:
            digits.append(x%10)
            x_temp = x//10

        for i,d in enumerate(digits[::-1]):
            p += d*(10**i)
            print(p)

        return p == x """
        return str(x) == str(x)[::-1]
