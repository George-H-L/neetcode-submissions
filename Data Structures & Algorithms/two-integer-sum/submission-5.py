class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map stores {number_we_have_seen : its_index}
        hash_map = {} 

        for k, v in enumerate(nums):
            if target - v in hash_map:
                return[hash_map[target - v], k]
            hash_map[v] = k