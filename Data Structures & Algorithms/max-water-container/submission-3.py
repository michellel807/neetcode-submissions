class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxarea = 0
        while right>left:
            area = min(heights[left], heights[right])*(right-left)
            print(area)
            
            if area>maxarea:
                maxarea = area
            
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        
        return maxarea