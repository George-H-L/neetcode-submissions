class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

nums = [1, 2, 3, 3]
solution = Solution()
result = solution.hasDuplicate(nums)
print(result)
