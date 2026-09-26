class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            first_idx = mid // n
            second_idx = mid % n

            if target < matrix[first_idx][second_idx]:
                right = mid - 1
            elif target > matrix[first_idx][second_idx]:
                left = mid + 1
            else:
                return True
        
        return False