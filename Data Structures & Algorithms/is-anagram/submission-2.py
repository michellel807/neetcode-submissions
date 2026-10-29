class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1 = {}
        counts2 = {}
        for char in s:
            if char not in counts1:
                counts1[char] = 1
            else:
                counts1[char] += 1
        
        for char in t:
            if char not in counts2:
                counts2[char] = 1
            else:
                counts2[char] += 1

        if counts1 == counts2:
            return True
        else:
            return False