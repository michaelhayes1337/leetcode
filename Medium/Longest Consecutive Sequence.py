from typing import List

class Solution:
    # didnt workd
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums)==0:
    #         return 0
    #     longest = set()
    #     sort = sorted(nums)
    #     length = 1;
    #     for i in range(len(nums)):
    #         if i > 0:
    #             if sort[i]-sort[i-1] == 1:
    #                 length += 1
    #             else:
    #                 longest.add(length)
    #                 length = 1
    #     longest.add(length)
    #     return max(longest)

    #brute force
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     f = set(nums)
    #     longest = 0
    #     for n in f:
    #         if (n-1) in f:
    #             continue
    #         else:
    #             curr = n+1
    #             while True:
    #                 if curr in f:
    #                     curr += 1
    #                 else:
    #                     break
    #             if curr-n > longest:
    #                 longest = curr-n
    #     return longest
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if (n-1) not in numSet:
                length = 1
                while (n + length ) in numSet:
                    length += 1
                longest = max(longest, length)
        return  longest
print(Solution.longestConsecutive(None, [1,2,0,1]))