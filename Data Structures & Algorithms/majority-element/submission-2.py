class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mx_cnt = 0
        ans = -1
        set_nums = set(nums)
        dict_nums = {num: nums.count(num) for num in set_nums}
        return sorted(dict_nums.items(), key = lambda item: item[1], reverse=True)[0][0]