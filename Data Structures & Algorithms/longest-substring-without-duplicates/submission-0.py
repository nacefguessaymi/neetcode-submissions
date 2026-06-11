class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        sub = set()
        best = 0
        while r < n:
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            best = max(best, r - l + 1)
            r += 1
        return best