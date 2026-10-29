class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l_s = []

        if len(s) != len(t):
            return False

        
        for i in s:
            l_s.append(i)
        for j in t:
            if j in l_s:
                l_s.remove(j)
        if len(l_s) == 0:
            return True
        else: 
            return False


        
        