class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}
        for ch in ransomNote:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1
        for ch in magazine:
            if ch in count:
                count[ch] -= 1
                if count[ch] == 0:
                    del count[ch]
        return len(count) == 0