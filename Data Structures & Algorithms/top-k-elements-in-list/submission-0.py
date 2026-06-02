class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)
        freqs = {}
        for num in sorted_nums:
            if num not in freqs:
                freqs[num] = sorted_nums.count(num)
        sorted_freqs = sorted(freqs, key=freqs.get, reverse=True)
        return sorted_freqs[:k]
        