class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        vals = nums.count(val)
        for i in range(vals):
            nums.remove(val)
        return len(nums)