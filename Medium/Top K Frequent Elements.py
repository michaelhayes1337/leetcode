from typing import List


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     seen = {}
    #     for num in nums:
    #         if num in seen:
    #             seen[num] +=1
    #         else:
    #             seen[num] =1
    #     answer = []
    #     for n in range(k):
    #         maxCount = 0
    #         maxNum = 0
    #         for num in seen:
    #             if seen[num] > maxCount:
    #                 maxNum = num
    #                 maxCount = seen[num]
    #         answer.append(maxNum)
    #         seen.pop(maxNum)
    #     return answer

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res




print(Solution.topKFrequent(None, [1,1,1,2,2,3,3,3,3,3], k = 2))