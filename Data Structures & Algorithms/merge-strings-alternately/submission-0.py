class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_s = ""
        if len(word1) > len(word2):
            l, r = 0, len(word2)
            while l < r:
                merged_s += word1[l] + word2[l]
                l += 1
            merged_s += word1[r:]
        else:
            l, r = 0, len(word1)
            while l < r:
                merged_s += word1[l] + word2[l]
                l += 1
            merged_s += word2[r:]
        return merged_s