class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        running_max = -1

        for i in range(len(arr) - 1, -1, -1):
            num = arr[i]

            arr[i] = running_max
            if num > running_max:
                running_max = num

        return arr        