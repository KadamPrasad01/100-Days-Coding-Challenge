class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        for jewel in jewels:
            for stone in stones:
                if(jewel == stone):
                    count+=1
        return count
