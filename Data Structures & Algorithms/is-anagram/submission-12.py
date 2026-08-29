class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = dict()
        for char in s:
            if char in freq:
                freq[char]+=1 
            else:
                freq[char]=1
        
        freq_t = dict()
        for char in t:
            if char in freq_t:
                freq_t[char]+=1
            else:
                freq_t[char]=1
        return freq_t == freq