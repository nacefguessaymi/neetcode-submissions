class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sorted(nums)
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                ans = seen.remove(num)
        return list(seen)[0]