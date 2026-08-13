from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = Counter(s)
        freq_t = Counter(t)

        longer = freq_s if len(s) > len(t) else freq_t
        for element in longer:
            if freq_t.get(element) != freq_s.get(element):
                return False

        return True