class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.split()
        count = 0
        for i in arr:
            count+=1
        return count
