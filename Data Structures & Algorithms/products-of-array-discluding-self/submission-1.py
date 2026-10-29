class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            prefix = nums[0: i]
            suffix = nums[i+1: len(nums)]
            pre_product = 1
            suf_product = 1

            for x in prefix:
                pre_product*= x
            
            for  z in suffix:
                suf_product*=z
            

            value = (pre_product*suf_product)
            output.append(value)
        
        nums = output
        return nums
           
        
        # go thru for loop, divide by the value 

