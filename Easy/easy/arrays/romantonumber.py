class Solution:
    def romanToInt(self, s: str) -> int:
        romanmap = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        i=0
        while i<len(s):
            if i+1<len(s) and romanmap.get(s[i])<romanmap.get(s[i+1]):
                res += romanmap.get(s[i+1])-romanmap.get(s[i])
                i+=2
            else:
                res += romanmap.get(s[i])
                i+=1
        return res
