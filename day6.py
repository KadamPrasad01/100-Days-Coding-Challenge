class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n = len(arr)
        if not arr:
            return []
        cand1 = None
        cand2 = None
        c1 = 0
        c2 = 0
        for i in arr:
            if(i == cand1):
                c1+=1
            elif(i == cand2):
                c2+=1
            elif(c1 == 0):
                cand1 = i
                c1 = 1
            elif(c2 == 0):
                cand2 = i
                c2 = 1
            else:
                c1-=1
                c2-=1
            
        result = []
        if(arr.count(cand1) > n//3):
            result.append(cand1)
        if(cand2 != cand1 and arr.count(cand2) > n//3):
            result.append(cand2)
    
        return sorted(result)
