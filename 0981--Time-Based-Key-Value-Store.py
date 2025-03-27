class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value,timestamp))
        

        


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.data.get(key,[])
        left = 0 
        right = len(values) - 1

        
        
       
       
        while left <= right:
            middle_idx        = (left + right) // 2
            middle_value:str  = values[middle_idx][0]
            middle_timestamp = values[middle_idx][1]

            if middle_timestamp <= timestamp:
                res = middle_value
                left = middle_idx + 1
            else:
                right = middle_idx - 1


            
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
