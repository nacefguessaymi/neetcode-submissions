class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        dups: bool = False
        for num in nums:
            if num not in seen:
                seen.append(num)
            else:
                dups = True
                break
        return dups