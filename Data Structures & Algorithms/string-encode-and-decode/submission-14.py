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
            while s[j] != "#": # obtain length of word (we need a loop becuase length could be more than a single digit)
                j += 1
            length = int(s[i:j]) 
            i = j + 1 # move i to start of word
            j += (length + 1) # move j to end of word
            res.append(s[i:j])
            i = j # move i to end of word so we can start with next word


        return res

