class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        maxr = -1
        for i in range(len(arr) - 1 , -1, -1):
            ans[i] = maxr
            maxr = max(arr[i], maxr)
        return ans