class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       # we want to use a sldiing window for ths to find mn array size
       # we want to check a left pointer, increment a right pointer and compare to total vlaue.

       total, l = 0, 0 
       res = float("inf")

       for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(r - l + 1, res)
            total -= nums[l]
            l +=1
       return 0 if res == float("inf") else res



