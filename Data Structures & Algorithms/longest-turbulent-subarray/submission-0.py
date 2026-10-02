class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        count = 1
        best = 1
        prev = "="
        if len(arr) < 2:
            return 1
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1] and prev != "<":
                prev = "<"
                count += 1
            elif arr[i] > arr[i-1] and prev != ">":
                prev = ">"
                count += 1
            elif arr[i] == arr[i-1]:
                prev = "="
                count = 1
            else:
                count = 2
            best = max(count, best)
        return best
