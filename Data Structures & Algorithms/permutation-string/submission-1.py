class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        while r<(len(s2)+1):
            s3 = s2[l:r]
            print(s3)
            sorts2 = sorted(s3)
            sorts1 = sorted(s1)
            
            if sorts1 == sorts2:
                return True
            else:
                l+=1
                r+=1
            print(l,r)
        return False
            