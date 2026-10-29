class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left1 = 0
        
        right = len(nums)-1
        sort_nums = sorted(nums)
        # -1 0 1 2 4
        output = []
        while left1<(len(nums)-1):
            left2 = left1 + 1
            while right>left2:
                sum =  sort_nums[left1] + sort_nums[right] + sort_nums[left2]
                if sum>0:
                    right-=1
                elif sum == 0:
                    if [sort_nums[left1], sort_nums[left2], sort_nums[right]] not in output:
                        output.append([sort_nums[left1], sort_nums[left2], sort_nums[right]])
                    left2+=1
                else:
                    left2+=1
            left1+=1
            right=len(nums)-1
        return output
                    