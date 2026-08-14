class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        p_to_w = {}
        w_to_p = {}
        for i in range(len(pattern)):
            ch = pattern[i]
            word = s[i]
            if len(pattern) != len(s):
                return False
            if ch in p_to_w and p_to_w[ch]!= word:
                return False
            if word in w_to_p and w_to_p[word]!= ch:
                return False
            p_to_w[ch] = word
            w_to_p[word] = ch
        return True
        