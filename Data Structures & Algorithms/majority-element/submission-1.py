class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mx_cnt = 0
        ans = -1
        set_nums = set(nums)
        for s in set_nums:
            if nums.count(s) > mx_cnt:
                mx_cnt = max(nums.count(s), ans)
                ans = s
        return ans