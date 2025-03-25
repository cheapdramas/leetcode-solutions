class Solution:
    def trap(self,height:list[int]) -> int:
        result = 0
        

        max_l = height[0]
        max_r = height[-1]
        
        left = 0
        right = len(height) - 1

        while left < right:
            if height[left]< max_l:
                result += max_l - height[left]
            elif height[right] < max_r: 
                result += max_r - height[right]
    
            if height[left] < height[right]:
                left += 1
            elif height[right] <= height[left]:
                right -= 1

            max_l = max(max_l,height[left])
            max_r = max(max_r,height[right]) 
        


        return result


