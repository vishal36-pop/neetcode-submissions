class TimeMap:

    def __init__(self):
        self.keystore = collections.defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        # our key is the key 
        #so now we have a sorted list of the timestamp,value accoring to timestamp
        if self.keystore[key] == []:
            return ''

        l,r = -1,len(self.keystore[key])-1

        while l<r:
            mid = (l+r+1)//2
            if self.keystore[key][mid][0] <= timestamp:
                l = mid
            else:
                r = mid-1
        if l == -1:
            return ''
        return self.keystore[key][l][1]
