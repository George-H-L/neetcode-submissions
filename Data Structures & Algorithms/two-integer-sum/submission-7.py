class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map stores {number_we_have_seen : its_index}
        map = {}

        for i, v in enumerate(nums):
            if target - v in map:
                return [map[target - v], i]
            map[v] = i