class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        dups: bool = False
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                dups = True
                break
        return dups