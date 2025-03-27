class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #O(n*m)
        haystack_len = len(haystack)
        needle_len = len(needle)

        if haystack_len < needle_len:
            return -1
        left = 0
        right = needle_len
        
        while True:
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
            if right > haystack_len:
                return -1
