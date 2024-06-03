class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        prev_1 = 2
        prev_2 = 1
        curr = 0
        for i in range(3, n+1):
            curr = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = curr
        return curr
    
sol = Solution()
print(sol.climbStairs(4))

# add previous 2 values. 