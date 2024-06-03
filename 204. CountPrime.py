import math 

class Solution:
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True 

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for num in range(2, int(math.sqrt(n)) + 1):
            if Solution.isPrime(num):
                for i in range(num*num, n, num):
                    primes[i] = False
        return sum(primes)  
    
s = Solution()
print(s.countPrimes(3))