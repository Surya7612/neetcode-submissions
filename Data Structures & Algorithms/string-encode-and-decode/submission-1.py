class Solution:

    def encode(self, strs: List[str]) -> str:
        # Format: "len#string" foe each string
        return ''.join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # read length prefix until we hit '#'
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res