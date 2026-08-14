class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grp = {}
        for word in strs:
            key = sorted(word)
            key = "".join(key)
            if key not in grp:
                grp[key] = [word]
            else:
                grp[key].append(word)
        return list(grp.values()) 

            
        
        

        