class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        # buckets[f] = list of numbers that appear exactly f times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in d.items():
            buckets[freq].append(num)

        # walk from highest frequency down, collect until we have k
        result = []
        for f in range(len(buckets) - 1, 0, -1):
            for num in buckets[f]:
                result.append(num)
                if len(result) == k:
                    return result
        return result