class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for i in range (len(strs)):
            while (strs[i].find(prefix)!=0):
                prefix=prefix[:len(prefix)-1]
                if not strs:
                    return ""
        return prefix
    