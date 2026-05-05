class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minString = 999999
        for s in strs:
            minString = min(minString , len(s))
        print(minString)

        prefix = ""
        for i in range(minString):
            prefix+=strs[0][i]
            for s in strs:
                print(prefix[i], s[i])
                if s[i]!= prefix[i]:
                    return prefix[:-1]
        return prefix