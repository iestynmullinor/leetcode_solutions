"""Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here."""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {}
        for letter in s:
            if not letter in d.keys():
                d[letter] = 1
            else:
                d[letter]+=1

        counts = d.values()

        longest = 0
        
        for i in range(len(counts)):
            while counts[i] >=2:
                longest+=2
                counts[i]-=2

        if any([x for x in counts if x > 0]):
            longest+=1
        
        return longest
    
