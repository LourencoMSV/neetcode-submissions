class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        l=0
        freq = {}
        maxF=0
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            maxF=max(maxF,freq[s[r]])
            while (r-l+1 - maxF > k):
                freq[s[l]] -=1
                l+=1
            result = max(result, r-l+1)
        return result