class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        freq = {}

        for s in s1:
            if s in freq:
                freq[s]+=1
            else:
                freq[s]=1
        n = len(s1)
        l = 0
        for r in range(len(s2)):
            curr = s2[r]
            if curr in freq and freq[curr]>0:
                freq[curr]-=1
            else:
                if curr in freq:
                    while freq[curr]==0:
                        freq[s2[l]]+=1
                        l+=1
                    freq[curr]-=1
                else:
                    while l<=r:
                        if s2[l] in freq:
                            freq[s2[l]]+=1
                        l+=1
            if r-l+1 == n:
                return True
        return False