class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < (len(s)-1):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + (length - 1)
            decoded.append(s[i:j+1])
            i = j + 1
            
        return decoded