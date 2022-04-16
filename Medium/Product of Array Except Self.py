from typing import List


class Solution:
    # too slow for requirements O(n^2)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     answer = []
    #     for i,val in enumerate(nums):
    #         product = 1
    #         for j, val2 in enumerate(nums):
    #             if j != i:
    #                 product *= val2
    #         answer.append(product)
    #     return answer

    # this is nice O(n) time and space
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        answer = []
        for n in nums:
            answer.append(prefix)
            prefix *= n
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer


print(Solution.productExceptSelf(None,[1,2,3,4]))