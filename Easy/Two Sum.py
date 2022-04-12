from typing import List


class Solution:
    # Run O(n) Space O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in seen:
                return (i,seen[remainder])
            seen[num] = i
        return (-1,-1)

print(Solution.twoSum(None, [2,7,11,15], 28))