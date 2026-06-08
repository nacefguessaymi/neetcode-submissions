class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = 0 
        l, r = height[i], height[j]
        while i < j:
            if l < r:
                i += 1
                l = max(l, height[i])
                area += l - height[i]
            else:
                j -= 1
                r = max(r, height[j])
                area += r - height[j]
        return area