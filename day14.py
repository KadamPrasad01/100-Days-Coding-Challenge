from collections import Counter
class Solution:
    def firstRep(self, s):
        # code here
        count = Counter(s)
        for char in count:
            if(count[char] > 1):
                return char
        return -1
