class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        left, right = 0, len(s1) - 1

        count = [0] * 26
        for i in range(len(s1)):
            count[ord('z') - ord(s1[i])] += 1

        curr_count = [0] * 26
        for i in range(right + 1):
            curr_count[ord('z') - ord(s2[i])] += 1

        while right + 1 < len(s2):

            if count == curr_count:
                return True

            curr_count[ord('z') - ord(s2[left])] -= 1
            left += 1
            right += 1
            curr_count[ord('z') - ord(s2[right])] += 1

        return True if count == curr_count else False
