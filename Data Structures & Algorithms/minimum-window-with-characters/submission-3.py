class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        aux = {}
        for x in t:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        l=0
        result = ""
        have = 0
        need = len(freq)
        resLen=math.inf
        for r in range(len(s)):
            curr = s[r]
            aux[curr] = aux.setdefault(curr,0)+1
            if curr in freq and freq[curr]==aux[curr]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    result = s[l:r+1]
                    resLen=r-l+1
                aux[s[l]]-=1
                if s[l] in freq and aux[s[l]]<freq[s[l]]:
                    have -=1
                l+=1
                    
        return result
                    