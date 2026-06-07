class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        x = list(s)
        z = list(t)

        slist = sorted(x)
        tlist = sorted(z)
        
        if slist == tlist:
            return True
        return False

solution = Solution()
s = "racecar"
t = "carrace"
result = solution.isAnagram(s,t)
print(result)