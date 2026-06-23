class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_set = set(sorted(nums))
        ans = []
        target = len(nums) / 3
        for num in nums_set:
            if nums.count(num) > target:
                ans.append(num)
        return ans
            
