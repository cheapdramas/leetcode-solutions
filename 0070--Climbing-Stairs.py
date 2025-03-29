class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        passed_ways = 3
        previous_passed_ways = 2

        curr = 0 

        for _ in range(3,n):
            curr = passed_ways + previous_passed_ways
            previous_passed_ways = passed_ways
            passed_ways = curr

        return curr

