class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hash map where value is the frequency!!!

        d = {}

       

        for v in nums:
            if v not in d:
                d[v] = 1
            elif v in d:
                d[v] += 1
        

        asc = OrderedDict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        kitems = list(asc.items())[:k]

        return [num for num, freq in kitems]
        

        