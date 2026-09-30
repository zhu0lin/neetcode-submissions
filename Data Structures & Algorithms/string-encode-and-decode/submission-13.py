class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            n = len(s)
            res.append(str(n))
            res.append("#")
            res.append(s)
            # "5#Hello5#World"

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            print(length)
            i = j + 1
            j += (length + 1)
            print(s[i:j])
            res.append(s[i:j])
            i = j


        return res

