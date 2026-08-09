class TimeMap:

    def __init__(self):
        self.timemap = {} # key: string, value: [(value, timestamp),...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((value,timestamp))
        else:
            self.timemap[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not self.timemap or key not in self.timemap:
            return ""
        value_list = self.timemap[key]
        l=0
        h=len(value_list)-1
        result = ""
        while l<=h:
            mid = (h+l) // 2
            if value_list[mid][1]<=timestamp:
                result=value_list[mid][0]
                l=mid+1
            else:
                h=mid-1

        return result