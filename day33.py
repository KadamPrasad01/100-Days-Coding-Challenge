class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        while(num >= 10):
            for digits in str(num):
                sum += int(digits)
            num = sum
        return num
