class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = [i for j in matrix for i in j]
        matrix = [True if i == target else False for i in matrix]
        matrix = set(matrix)
        return True if True in matrix else False