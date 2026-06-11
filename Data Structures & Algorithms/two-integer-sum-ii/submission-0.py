class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize pointers at the very beginning and very end of the array
        left = 0
        right = len(numbers) - 1

        # Loop until the two pointers meet
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Add 1 to both indices if the platform expects 1-indexed answers
                return [left + 1, right + 1]
                
            elif current_sum < target:
                # The sum is too small. Move the left pointer to the right to get a bigger number.
                left += 1
                
            else:
                # The sum is too big. Move the right pointer to the left to get a smaller number.
                right -= 1