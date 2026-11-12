class TimeMap:

    def __init__(self):
        self.t_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t_map:
            self.t_map[key] = [(value,timestamp)]
        else:
            self.t_map[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        best = ""

        if key not in self.t_map:
            return best

        l, r = 0, len(self.t_map[key]) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            if self.t_map[key][mid][1] <= timestamp:
                best = self.t_map[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return best
