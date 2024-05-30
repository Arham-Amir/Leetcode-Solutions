
class Solution(object):
    @classmethod
    def mulResultOfElements(cls, nums):
        result = 0
        for num in nums:
            if num != 0:
                if result == 0:
                    result = num
                else:
                    result *= num
        return result  
    
    @staticmethod
    def productExceptSelf(nums):
        indices_of_zero = [i for i, num in enumerate(nums) if num == 0]
        if len(indices_of_zero)<2:
            sum = Solution.mulResultOfElements(nums)
            if len(indices_of_zero) == 0:
                result = list(map(lambda n: sum//n if n!=0 else sum, nums))
            else:
                result = [0]*len(nums)
                for i in indices_of_zero:
                    result[i] = sum
            return result
        else:
            return [0]*len(nums)
print(Solution.productExceptSelf([1,2,3,4]))
        