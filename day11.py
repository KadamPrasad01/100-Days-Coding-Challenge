class Solution:

	def segregateEvenOdd(self,arr):
		# code here
		even = []
		odd = []
		for i in arr:
		    if(i % 2 == 0):
		        even.append(i)
		    else:
		        odd.append(i)
		even.sort()
		odd.sort()
		arr[:] = even + odd
		return arr
		
