class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums[:-2]):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            
            j, k = i + 1 , len(nums) - 1
            while j < k:
                ijk_sum = num + nums[j] + nums[k]
                if ijk_sum == 0:
                    ans.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif ijk_sum < 0:
                    j += 1
                elif ijk_sum > 0:
                    k -= 1
        return ans
