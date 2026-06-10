class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {position[i]: speed[i] for i in range(len(speed))}
        cars = dict(sorted(cars.items(), reverse=True))
        stack = []
        for car, spe in cars.items():
            stack.append((target - car)/spe)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)