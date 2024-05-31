class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        pow = abs(n)
        while pow>0:
            if pow%2== 1:
                result *= x
            x *= x
            pow //= 2
        return result if n>0 else 1/result

sol = Solution()
print(sol.myPow(2, 5))