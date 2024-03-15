
#O(M) where M is the size of the patter
def construct_table(pattern):

	#constructing the "bad match table": we need the pattern 
	length_pattern = len(pattern)
	#the table is a dictionary - {char:number of shifts} values
	bad_match_table = {}

	#consider all the letters of the pattern
	for index,character in enumerate(pattern):
		#use the this formula to calculate the shift value for all the letters in the pattern
		max_shift = max(1,length_pattern-index-1)
		#insert the shift value with the character accordingly (or update if needed)
		bad_match_table[character] = max_shift
		
	return bad_match_table

#Boyer-Moore algorithm to find the pattern in the text
def search(text, pattern):

	#first we need the "bad match table"
	table = construct_table(pattern)
	
	length_text = len(text)
	length_pattern = len(pattern)
	
	#index i will track the letters of the text
	i=0

	#we consider all the letters in the text (OK not all of them because we may skip multiple letters)
	while i<=length_text-length_pattern:
	
		#number of skips is 0 at the beginning
		num_skips = 0
		
		#consider the pattern in reverse order
		for j in range(length_pattern-1,-1,-1):
	
			#if there is a mismatch we have to update the value of the num_skips
			if text[i+j] != pattern[j]:

				#the "bad match table" contains the letter in the text 
				if text[i+j] in table:
					num_skips = table[text[i+j]]					
				#otherwise the num_shift = number of letters in the pattern
				else:
					num_skips = length_pattern
					
				i = i + num_skips
				#the characters are not matching so no need to consider further letters
				break			
		
		#if all the letters are matching (letters in text and pattern accordingly) we find the pattern		
		if num_skips == 0: return i

	#the pattern is not found in the text 
	return -1
	
if __name__ == "__main__":
	
	print(search("this is a test","Adam"))
	
	