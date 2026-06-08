class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict()

        for char in s:
            if char in count:
                count[char] = count[char]+1
            else:
                count[char] = 1
        
        for char in t:
            if char in count:
                count[char] = count[char] -1
                if count[char] ==0:
                    del count[char]
            else:
                return False
        
        return len(count)==0