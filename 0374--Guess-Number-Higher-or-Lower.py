class Solution:
    def guessNumber(self, n: int) -> int:
        
        l = 1
        r = n
        while l <= r:
            m = (l + r) // 2
            res = guess(m) 
            
            if res == 0:
                return m  
            elif res > 0:
                l = m + 1  
            else:
                r = m - 1
