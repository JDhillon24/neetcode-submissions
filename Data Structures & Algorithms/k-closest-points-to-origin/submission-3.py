class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        squareCoords = lambda x: x[0] ** 2 + x[1] ** 2

        def kClosestHelper(points: List[List[int]], s: int, e: int, k: int) -> List[List[int]]:
            if (e - s + 1 <= 1):
                return points
            

            pivot = points[e]
            left = s

            for i in range(s, e):
                if squareCoords(points[i]) < squareCoords(pivot):
                    tmp = points[left]
                    points[left] = points[i]
                    points[i] = tmp
                    left += 1
            
            points[e] = points[left]
            points[left] = pivot

            # pivot is at k elems, array is sorted
            if left == k - 1:
                return
            # pivot is greater than k elems, right side is too big
            elif left > k - 1:
                kClosestHelper(points, s, left - 1, k)
            # pivot is less than k elems, need more elements
            else:
                kClosestHelper(points, left + 1, e, k)
        

        kClosestHelper(points, 0, len(points) - 1, k)




        return points[:k]