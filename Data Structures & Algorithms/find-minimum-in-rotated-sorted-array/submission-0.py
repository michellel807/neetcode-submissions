class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while right>left:
            middleval = nums[(right-left)//2]
            middle = left + (right-left)//2
            
            if nums[right]>nums[middle]:
                right = middle
            else:
                left = middle+1
        return nums[left]
