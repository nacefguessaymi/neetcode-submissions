class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        mappin = {")": "(", "]": "[", "}": "{"}
        tra = []
        while i < len(s):
            if s[i] in mappin.keys():
                if tra and tra[-1] == mappin[s[i]]:
                    tra.pop()
                else:
                    return False
            else:
                tra.append(s[i])
            i += 1
        return True if not tra else False
