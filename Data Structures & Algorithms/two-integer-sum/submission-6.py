class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map stores {number_we_have_seen : its_index}
       HASH = {}

       for i,v in enumerate(nums):
        diff = target - v
        if diff in HASH:
            return [HASH[diff],i]
        HASH[v] = i
        