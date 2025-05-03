class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(arr)):
            if(arr[i] % 2 != 0):
                count+=1
                if(count == 3):
                    return True
                    break
            else:
                count = 0
        return False
        
