class Solution(object):
    def reverseWords(self, s):
        result = s.split(" ")
        print(result)
        result = list(filter(lambda a: a!="", result))
        return " ".join(list(reversed(result)) )
        
solution = Solution()
print(solution.reverseWords("Hello  World")) 