class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        nmap = {}
        rmap = {}
        for i in range(len(s)):
            s_ch = s[i]
            t_ch = t[i]
            if s_ch in nmap and nmap[s_ch] != t_ch:
                return False
            if t_ch in rmap and rmap[t_ch] != s_ch:
                return False
            nmap[s_ch] = t_ch
            rmap[t_ch] = s_ch
        return True
                

        