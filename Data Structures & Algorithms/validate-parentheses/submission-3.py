class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "{":"}", "[":"]"}
        seen = []

        #([{}])
        for i in range(len(s)):
            par = s[i]
            if par in pairs: #a key
                seen.append(par)
            else:
                if not seen:
                    return False
                if pairs[seen[-1]] != par:
                    return False
                seen.pop()
        
        if len(seen) == 0:
            return True
        else:
            return False