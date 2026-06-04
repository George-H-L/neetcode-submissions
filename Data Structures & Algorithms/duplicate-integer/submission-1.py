class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()
        #integer array - nums, record hash map compare values

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

nums = [1, 2, 3, 3]
solution = Solution()
result = solution.hasDuplicate(nums)
print(result)
