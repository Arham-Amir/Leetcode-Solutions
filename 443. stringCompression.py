class Solution(object):
    def compress(self, chars):
        result = []
        count = 1
        for i in range(len(chars)):
            if i < len(chars)-1 and chars[i] == chars[i+1]:
                count+=1
            else:
                result.append(chars[i])
                if count> 1:
                    result.extend(list(str(count)))
                count = 1
        return result
        
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))