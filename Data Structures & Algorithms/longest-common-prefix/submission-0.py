class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            result+=char
            for string in strs:
                if len(string)>i and string[i]==char:
                    continue
                else:
                    result=result[:-1]
                    return result
                
        return result