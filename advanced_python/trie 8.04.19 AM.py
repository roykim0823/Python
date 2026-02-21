
ALPHABET_SIZE = 26

#the node in the tree structure (a node may contain given value - like a dictionary)
class Node:

	def __init__(self, character):
		#nodes are characters in a trie
		self.character = character
		#every node may have several children - this is why tries are not memory-efficient
		#every node has 26 children no matter they are needed or not
		self.children = [None for _ in range(ALPHABET_SIZE)]
		#we have to track whether a given node is a leaf node or not 
		#leaf nodes are the end of given words in the tree
		self.leaf = False
		
class Trie:

	def __init__(self):
		#the root node is an empty node (here we use *)
		self.root = Node('*')
		
	#inserting an item takes O(M) time where M is the size of the word we insert
	def insert(self,word):
	
		#always start at the root node
		current = self.root

		#consider all the letters of the word
		for char in word:

			#we are dealing with indexes: use ASCII representation to get the index and transform
			#within the range [0,ALPHABET_SIZE-1]
			ascii_index = ord(char)-ord('a')				
		
			#there may be a child with the given letter
			if current.children[ascii_index]:
				#we keep going
				current = current.children[ascii_index]
			else:
				#otherwise we insert a new node with the given character
				node = Node(char)
				current.children[ascii_index] = node
				current = node

		#after we considered all the letters of the word ... it is the end of a word
		#leaf nodes represent end of words in the tree
		current.leaf = True
	
	#checks whether given word is present in the tree or not [running time is O(M)]
	def search(self, word):
	
		#if the tree is empty we return false
		if not self.root.children:
			return False
			
		#always start with the root node
		current = self.root
	
		#consider all the letters of the word
		for char in word:
		
			#we are dealing with indexes: use ASCII representation to get the index and transform
			#within the range [0,ALPHABET_SIZE-1]
			ascii_index = ord(char)-ord('a')
		
			#the given letter is present in the tree (so there is a valid child)
			if current.children[ascii_index]:
				#then we keep going
				current = current.children[ascii_index]
			else:
				#otherwise we know the word is not present in the tree
				return False
	
		#if we've considered all the letters and the actual node is a leaf node: we found the word
		if current.leaf:
			return True

		#word is not present in the tree
		return False
		
	def sort(self):
	
		#if the root is not a None (so trie is not empty)
		if self.root:
			return self.get_words_prefix('')			
	
	#finding the longest common prefix (important in IP routing)
	def longest_common_prefix(self):
	
		#we start with the (*) root node
		current_node = self.root
		#this string represents the longest common prefix (lcp)
		lcp = ''
		
		#we iterate until the node is a leaf node
		while not current_node.leaf:
		
			#have to calculate the number of children (and the index of that node)
			num_children,child_index = self.count_children(current_node)
			
			#if there are more then 1 children: we have to stop
			if num_children!=1:
				break
				
			#consider the next node (so the child of the current one)
			current_node = current_node.children[child_index]
			#keep building the longest common prefix (lcp) character by character
			lcp = lcp + str(current_node.character)
			
		return lcp
		
	#helper function for longest common prefix problem
	def count_children(self, node):
	
		num_children = 0
		child_index = 0
	
		#calculate the number of children + store the index
		for index,child in enumerate(node.children):
			if child:
				num_children = num_children + 1
				child_index = index
	
		return num_children,child_index
	
	#Google's Search Algorithm: when we start typing Google show the suggestions
	#so let's gather the words with the same prefix
	def get_words_prefix(self, prefix):
	
		#always start with the root node
		node = self.root

		#we store the words in a list
		all_words = []
		
		#consider the letters in the prefix one by one
		#so we find the node associated with the last letter of the prefix
		for char in prefix:
		
			#we are dealing with indexes: use ASCII representation to get the index and transform
			#within the range [0,ALPHABET_SIZE-1]
			ascii_index = ord(char)-ord('a')
		
			#if there is no solution (for example words: [flower,flow,flight] and prefix is 'adam')
			if not node.children[ascii_index]:
				return None
		
			node = node.children[ascii_index]
			
		#then we collects all the words starting with the same prefix
		self.collect(node,prefix,all_words)
		
		return all_words
		
	def collect(self, node, prefix, all_words):
	
		#recursive implementation so this is the base case
		if not node:
			return
			
		#leaf nodes represent valid words so we put them into the array
		if node.leaf:
			#node we keep appending letters to the prefix (so this prefix is not the original prefix any more)
			all_words.append(prefix)
			
		#keep going and consider the next layers
		for child in node.children:
			#if the child is None we consider the next child (on the same level)
			if not child:
				continue
				
			#we keep going down ... append the next letter to the prefix and 
			#call the function recursively
			child_character = child.character
			
			self.collect(child,prefix+child_character,all_words)
		
if __name__ == "__main__":
	
	trie = Trie()
	
	trie.insert('sea')
	trie.insert('seashore')
	
	print(trie.longest_common_prefix())