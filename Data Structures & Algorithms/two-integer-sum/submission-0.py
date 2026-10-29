class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            for next_index in range(index+1, len(nums)):
                if nums[index]+nums[next_index] == target:
                    return [index, next_index]
            
