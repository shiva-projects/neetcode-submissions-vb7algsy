class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_index = [0] * 26
        for i in s:
            char_index[ord(i) - ord('a')] += 1
        for i in t:
            char_index[ord(i) - ord('a')] -= 1
        if char_index == [0] * 26:
            return True
        return False