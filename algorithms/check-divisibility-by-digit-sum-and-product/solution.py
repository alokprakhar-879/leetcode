class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        s = 0
        m = 1

        while n > 0:
            digit = n % 10
            s += digit
            m *= digit
            n //= 10

        return original % (s + m) == 0