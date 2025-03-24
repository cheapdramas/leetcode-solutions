class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        nums_len = len(nums)


        for index,num in enumerate(nums):
            if index and num == nums[index - 1]:
                continue
    
            left = index + 1
            right = nums_len - 1
            
            while left < right: 
                three_sum = num + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([num,nums[left],nums[right]])
                    left += 1
                    while left == nums[left - 1] and left < right:
                        left += 1
            





        return result 
