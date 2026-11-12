class TimeMap:

    def __init__(self):
        
        self.store = {} # key: the given key, val will be a tuple, these will be ordered by timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp,value)]
        else:
            self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        else:
            store_list = self.store[key]
            l=0
            r=len(store_list)-1
            res = ""
            while l<=r:
                mid = l+(r-l)//2
                if store_list[mid][0]==timestamp:
                    return store_list[mid][1]
                elif store_list[mid][0]>timestamp:
                    r=mid-1
                else:
                    l=mid+1
                    res=store_list[mid][1]
            return res