class Solution:
    # Run O(n) Space O(1)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if sorted(s) == sorted(t):
    #         return True
    #     return False

    # Run O(n) Space O(n)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) == len(t):
    #         charSet = set(s)
    #         for char in charSet:
    #             if s.count(char) != t.count(char):
    #                 return False
    #         return True

    # Run O(n) Space O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            chars = {}
            for c in s:
                if c in chars:
                    chars[c] += 1
                else:
                    chars[c] = 1
            for c in chars:
                if chars[c] != t.count(c):
                    return False
            return True

    # Run O(n) Space O(n)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) == len(t):
    #         hashS = {}
    #         hashT = {}
    #         for i in range(len(s)):
    #             charS = s[i]
    #             charT = t[i]
    #             if charS in hashS:
    #                 hashS[charS] += 1
    #             else:
    #                 hashS[charS]= 1
    #             if charT in hashT:
    #                 hashT[charT] += 1
    #             else:
    #                 hashT[charT]= 1
    #         if hashS == hashT:
    #             return True
    #     return False



print(Solution.isAnagram(None,s="anagram", t="nagaram"))