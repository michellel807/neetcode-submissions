class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while r>=l:
            mid = (l+r)//2
            row_mid = matrix[mid]
            print(row_mid)
            if row_mid[0] > target:
                r = mid-1
            
            elif row_mid[-1] < target:
                l = mid+1

            else:
                print(l,r)
                left = 0
                right = len(row_mid)-1
               
                while right>=left:
                    middle = (left+right)//2
                    if row_mid[middle]>target:
                        right = middle-1
                    elif row_mid[middle]<target:
                        left = middle+1
                    else: 
                        return True
                    print(middle)
                return False
        return False
        
            
