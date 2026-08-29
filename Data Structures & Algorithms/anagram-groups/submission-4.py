class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}  # freq maps as key, list of strings as values

        for string in strs:
            freq = [0]*26
            for char in string:
                freq[ord(char)-ord('a')]+=1
            freq = tuple(freq)
            if freq in res:
                res[freq].append(string)
            else:
                res[freq]=[string]
        return list(res.values())

