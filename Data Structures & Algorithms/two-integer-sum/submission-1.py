class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_left = [target - num for num in nums]
        for i, num in enumerate(nums_left):
            if num in nums and nums.index(num) != i:
                return [min(i, nums.index(num)), max(i, nums.index(num))]