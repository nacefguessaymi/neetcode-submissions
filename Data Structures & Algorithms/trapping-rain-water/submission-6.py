class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0 
        for i in range(len(height)):
            l = height[:i]
            r = height[i:]
            l = max(max(l), height[i]) if l else height[i]
            r = max(max(r), height[i]) if r else height[i]
            area += min(l, r) - height[i]
        return area