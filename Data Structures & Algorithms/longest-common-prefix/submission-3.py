class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort(key=len)
        for i, s in enumerate(strs[0]):
            for oth_s in strs[1:]:
                if oth_s[i] != s:
                    return ans
            ans += s
        return ans