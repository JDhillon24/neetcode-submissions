class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low + high) // 2

            first_idx = mid // n
            second_idx = mid % n

            if matrix[first_idx][second_idx] < target:
                low = mid + 1
            elif matrix[first_idx][second_idx] > target:
                high = mid - 1
            else:
                return True
        
        return False