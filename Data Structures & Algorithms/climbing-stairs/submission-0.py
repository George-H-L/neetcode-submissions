class Solution:
    def climbStairs(self, n: int) -> int:
        
        # n times at default, we can add 1 immediately, if n % 2 == 0, then we cna do n/2 times aswell. 
        # 1 - 1 way, 2 - 2 ways, 3 - 3 ways, 4 - 5 ways. 5 - 8 ways. recursion, each step is one way more than the last, or if even its two steps more.

     
        memo = {}

        for i in range(0, n+1):
            if i <2:
                result = 1
            else:
                result = memo[i-1] + memo[i-2]
            memo [i] = result
        return memo[i]

        