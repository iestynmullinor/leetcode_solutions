class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        #return true if s is a subsequence of t
        for s_char in s:

            #false if character from s is not in t
            if not s_char in t:
                return False
            
            position = t.index(s_char)
            t = t[position+1:]
        
        return True


