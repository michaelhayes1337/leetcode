from typing import List


class Solution:
    # Run O(n) Space O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

print(Solution.containsDuplicate(None,[1,2,3,1]))