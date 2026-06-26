class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,1

        used = dict()
        max_length=0
        first = 0
        for i,char in enumerate(s):
            if char not in used:
                used[char]=i
            else:
                index = used[char]
                if index+1>first:
                    first = index+1
                    l=first
                else:
                    l=first
                used[char] = i
            max_length = max(r-l, max_length)
            r+=1
        
        return max_length