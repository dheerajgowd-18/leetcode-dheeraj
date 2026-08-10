class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        char = list(s)
        for i in range(0,len(s),2*k):
            char[i:i+k] = char[i:i+k][::-1]
        return "".join(char)
             
            
