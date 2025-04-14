from collections import Counter
class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        counter = Counter(arr)
        for key in counter:
            if(counter[key] % 2!= 0):
                return key
-----------------------------------------------
from collections import Counter
class Solution:
    def longest(self, arr):
        # code here
        length =0
        str = ""
        for i in arr:
            if(len(i) > length):
                length = len(i)
                str = i
        return str
-------------------------------------------------
from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        reverse = arr[::-1]
        if(arr == reverse):
            return True
        else:
            return False
------------------------------------------
class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        arr2 = []
        present = True
        for i in range(A,B+1):
            arr2.append(i)
        for ele in arr2:
            if ele not in arr:
                present = False
        return present
---------------------------------------------------
class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        total = 0
        if(date%2 == 0):
            for i in range(len(fine)):
                if(car[i] % 2 != 0):
                    total+= fine[i]
        else:
            for i in range(len(fine)):
                if(car[i] % 2 == 0):
                    total+= fine[i]
        return total
                    
