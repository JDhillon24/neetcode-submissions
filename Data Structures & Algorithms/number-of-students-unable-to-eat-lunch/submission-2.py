class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        student_map = {}
        res = len(students)
        student_map[0] = 0
        student_map[1] = 0

        for s in students:
            student_map[s] = 1 + student_map.get(s, 0)
        
        for s in sandwiches:
            if student_map[s] > 0:
                res -= 1
                student_map[s] -= 1
            else:
                break
        
        return res

        