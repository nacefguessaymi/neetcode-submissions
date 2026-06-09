class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for i, temp in enumerate(temperatures):
            stack = temperatures[i:]
            stack = [t > temp for t in stack]
            if True in stack: 
                ans.append(stack.index(True)) 
            else: 
                ans.append(0) 
        return ans
