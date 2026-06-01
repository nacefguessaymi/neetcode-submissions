class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        if len(s) != len(t):
            return False
        for i, char in enumerate(list(s)):
            if char in hash_s:
                hash_s[char] +=1
            else:
                hash_s[char] = 1
            if t[i] in hash_t:
                hash_t[t[i]] += 1
            else:
                hash_t[t[i]] = 1
        for key, value in hash_t.items():
            if key not in hash_s:
                return False
                break
            if hash_s[key] != value:
                return False
                break
        return True
            
        