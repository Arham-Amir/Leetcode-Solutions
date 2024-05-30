from cmath import inf

class Solution(object):
    def increasingTriplet(self, nums):
        first, second = inf, inf
        for num in nums:
            if num <= first:
                first = num
            elif num<= second:
                second = num
            else:
                return True
        return False
        
        
s = Solution()
print(s.increasingTriplet([5,4,3,2,1]))
print(s.increasingTriplet([2,1,5,0,4,6]))
print(s.increasingTriplet([20,100,10,12,5,13]))