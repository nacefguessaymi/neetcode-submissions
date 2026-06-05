class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            new_numbers = numbers.copy()
            del new_numbers[:i]
            for oth_num in new_numbers:
                if  num + oth_num == target:
                    return [i+1, numbers.index(oth_num) + 1]