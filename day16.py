class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

-------------------------------------------
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        sum = s + s
        if(len(s) != len(goal)):
            return False
        return goal in sum
----------------------------------------------
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False
        mapping = {}
        mapped = set()

        for sc,tc in zip(s,t):
            if sc in mapping:
                if(mapping[sc] != tc):
                    return False
            else:
                if(tc in mapped):
                    return False
                mapping[sc] = tc
                mapped.add(tc)
        return True
