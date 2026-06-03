class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.replace(" ", "").replace("?", "").replace(".", "").replace("!", "").replace(",", "").replace("'", "").replace(":", "").lower()
        mid = len(new_s) // 2
        for i, c in enumerate(new_s[:mid]):
            if c == new_s[-(i + 1)]:
                continue
            else: 
                return False
        return True