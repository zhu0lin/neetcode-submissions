from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        # dic will look something like
        # {{a: 1, b:1, c:1} : [abc, bac, cab], ...}

        # i figured out we cant use a dictionary as keys to dictionaries
        # so we'll just flip the key and values 
        # our dic will look like
        # {[abc, bac, cab]: {a:1, b:1, c:1}}

        for string in strs:
            ord_arr = [0] * 26
            for char in string:
                ord_arr[(ord('z') - ord(char))] += 1
            dic[tuple(ord_arr)].append(string)
            # if tuple(ord_arr) in dic:
            #     dic[ord_arr].append(string)
            # else:
            #     dic[ord_arr] = [string]

        return list(dic.values())