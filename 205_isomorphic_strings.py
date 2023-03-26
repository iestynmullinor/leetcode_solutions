class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

    

        def find_map(chars):
            map = []
            positions = []

            for i in range(len(chars)):
                if not chars[i] in positions:
                    positions.append(chars[i])
                    map.append(i)
                
                else:
                    map.append(positions.index(chars[i]))
            return map

        return (find_map(s)==find_map(t))

            

            
            



