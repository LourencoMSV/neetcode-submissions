class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
        
        f = [[] for i in range(len(nums)+1)]
        for key,v in freq.items():
            f[v].append(key)

        res = []
        for i in range(len(f)-1,0,-1):
            for n in f[i]:
                res.append(n)
                if len(res)==k:
                    return res
        return []