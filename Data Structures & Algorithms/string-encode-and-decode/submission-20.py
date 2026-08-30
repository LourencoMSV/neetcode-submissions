class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        for s in strs:
            l = len(s)
            encoded_string+=str(l)+"€"+s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []
        while i < len(s):
            j = i
            while s[j]!="€":
                j+=1
            l = int(s[i:j])
            i=j+1
            j=i+l
            string = s[i:j]
            decoded_strs.append(string)
            i=j
        return decoded_strs