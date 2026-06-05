class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        srt_str = ["".join(sorted(stri)) for stri in strs]
        anas = {}
        for i, stri in enumerate(srt_str):
            if stri not in anas:
                anas[stri] = []
            anas[stri].append(strs[i])
        return list(anas.values())