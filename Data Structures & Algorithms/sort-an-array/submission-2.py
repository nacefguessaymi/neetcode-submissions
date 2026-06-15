from statistics import median
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        pivot = median([nums[0], nums[-1], nums[len(nums)//2]])
        less = list(filter(lambda x: x < pivot, nums))
        same = list(filter(lambda x : x == pivot, nums))
        greater = list(filter(lambda x : x > pivot, nums))
        return Solution.sortArray(self, less) + same + Solution.sortArray(self, greater)