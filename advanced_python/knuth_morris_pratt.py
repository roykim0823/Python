
#O(M) where M is the size of the patter
def construct_pi_table(pattern):

	#the table has as many values as the length of the pattern (first item is always a 0)
	pi_table = [0]*len(pattern)
	
	index = 0
	
	#it has O(M) running time so a single for loop
	for i in range(1,len(pattern)):
	
		if pattern[i] == pattern[index]:
			pi_table[i] = index + 1
			index=index+1
			i=i+1
		
		else:
			if index != 0:
				index = pi_table[index-1]
			else:
				pi_table[i] = 0
				i=i+1
				
	return pi_table

#Knuth-Morris-Pratt algorithm with O(N+M) running time
def search(text, pattern):

	#first we need the pi table
	pi_table = construct_pi_table(pattern)
	
	#index i tracks the text - index j tracks the pattern
	i = 0
	j = 0
	
	#we have to iterate until the i index is less than the N length of the text 
	#and we have to make sure j is smaller than the M length of the pattern
	while i<len(text) and j<len(pattern):
		
		#if the letters are matching we increment both indexes
		if text[i] == pattern[j]:
			i = i+1
			j = j+1
		
		#we found the pattern in the text (+ reinitialize the j index to be able find more patterns)
		if j==len(pattern):
			print("Pattern found at index ",str(i-j))
			j = pi_table[j-1]
		
		#if there is a mismatch
		elif i<len(text) and text[i]!=pattern[j]:
			#if we can decrement j then we decrement it based on the pi table
			if j!=0:
				j = pi_table[j-1]
			#if we are not able to decrement the j (because it has value 0) we increment i
			else:
				i=i+1
	
if __name__ == "__main__":
	
	search("this test is a test","is")
	
	