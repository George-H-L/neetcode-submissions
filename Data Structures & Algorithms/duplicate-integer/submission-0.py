class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = {}
        #integer array - nums, record hash map compare values

        for i, num in enumerate(nums):
            if num in seen:
                return True 
            seen[num] = i
        return False

nums = [1, 2, 3, 3]
solution = Solution()
result = solution.hasDuplicate(nums)
print(result)
