class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sum = {}
        # {0: 3, 1 : 4 , 2 : 5, 3 : 6}
        

        for i, num in enumerate(nums):
            num1 = target - num

            if num1 in sum:
                output = [sum[num1], i]

            sum[num] = i

        return output 

