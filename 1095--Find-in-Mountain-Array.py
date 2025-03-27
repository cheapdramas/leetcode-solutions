"""
This is MountainArray's API interface.
You should not implement it, or speculate about its implementation
"""
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:

    def find_peak(self):
        left = 1
        right = self.arr_len - 2
        while left <= right:
            mid = (left + right) // 2
            middle_value = self.arr.get(mid)
            before_mid_val = self.arr.get(mid - 1)
            after_mid_val = self.arr.get(mid + 1)



            
            if before_mid_val<middle_value<after_mid_val:
                left = mid + 1 
                
            elif before_mid_val>middle_value>after_mid_val:
                right = mid - 1
            else:
                return mid

    def binary_search(
        self,
        start:     int,
        end:       int,
        asc: bool
    ) -> Optional[int]:
        left = start
        right = end

        while left<= right:
            mid = (left + right) // 2
            mid_value = self.arr.get(mid)




            if mid_value > self.target:
                if asc:
                    right = mid - 1
                else:
                    left = mid + 1
            elif mid_value < self.target:
                if asc:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # equals
                return mid

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        self.arr = mountainArr
        self.arr_len = mountainArr.length()
        self.target = target

        peak = self.find_peak()

        result = self.binary_search(0,peak,False)
        if result is not None:
            return result 
        result = self.binary_search(peak,self.arr_len,True)
        if result is not None:
            return result 



        return -1
