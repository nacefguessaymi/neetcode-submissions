class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            new_nums = nums.copy()
            new_nums.pop(i)
            prod = 1
            for j in new_nums:
                prod = prod * j
            ans.append(prod)
        return ans