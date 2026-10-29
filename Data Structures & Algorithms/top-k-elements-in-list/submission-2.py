class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = 0
        dictionary = {}
        output = []
        for i in range(len(nums)):
            num = nums[i]
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        
        while count<k:
            maxval= 0 
            maxkey = 0
            for key in dictionary:
                if dictionary[key] > maxval:
                    maxkey = key
                    maxval = dictionary[key]
            count+=1
            output.append(maxkey)
            dictionary.pop(maxkey)
            
        return output
                