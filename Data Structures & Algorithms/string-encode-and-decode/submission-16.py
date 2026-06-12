class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string=encoded_string+"§§"+s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        split = s.split("§§")
        return split[1:]