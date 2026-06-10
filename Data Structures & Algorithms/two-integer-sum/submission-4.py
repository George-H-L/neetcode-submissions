class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map stores {number_we_have_seen : its_index}
        hash_map = {} 

        for k, v in enumerate(nums):
            diff = target - v

            # Check if we have already seen the number we need
            if diff in hash_map:
                # Return the index of the diff, and the current index 'k'
                return [hash_map[diff], k]
            
            # We haven't seen it, so add the current number and its index to the map
            hash_map[v] = k