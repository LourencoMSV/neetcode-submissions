class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:

            l = s[left]
            r = s[right]
            while not l.isalnum() and left<right:
                left +=1
                l = s[left]
            while not r.isalnum()and left<right:
                right-=1
                r = s[right]
            print(r.lower())
            print(l.lower())
            if r.lower()==l.lower():
                left+=1
                right-=1
            else:
                return False

        return True