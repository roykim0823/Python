
def search(text, pattern):

	#length of the text is N
	length_text = len(text)
	#length of the pattern is M
	length_pattern = len(pattern)

	#we consider all the letters in the text O(N) complexity
	for i in range(length_text):
	
		#we check the pattern (it is misleading it has O(M) running time)
		#that why (worst case) running time complexity of brute force search is O(N*M)
		if text[i:length_pattern+i] == pattern:
			#we find a match and return with the index
			return i
			
	#we do not find the pattern in the text
	return -1

if __name__ == "__main__":
	
	print(search("My name is Adam","Adam"))
	
	