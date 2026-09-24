import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def calculateSquares(x1: int, y1: int) -> float:
            square_x = x1 ** 2
            square_y = y1 ** 2

            return math.sqrt(square_x + square_y)

        
        def kClosestHelper(points: List[List[int]], s: int, e: int) -> List[List[int]]:
            if (e - s + 1) <= 1:
                return points
            
            pivot = points[e]
            left = s

            for i in range(s, e):
                point_calc = calculateSquares(points[i][0], points[i][1])
                pivot_calc = calculateSquares(pivot[0], pivot[1])

                if point_calc < pivot_calc:
                    tmp = points[left]
                    points[left] = points[i]
                    points[i] = tmp
                    left += 1
            
            points[e] = points[left]
            points[left] = pivot

            kClosestHelper(points, s, left - 1)
            kClosestHelper(points, left + 1, e)
        
        kClosestHelper(points, 0, len(points) - 1)

        return points[:k]


        

