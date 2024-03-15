
ALPHABET_SIZE = 26

#the node in the tree structure (a node may contain given value - like a dictionary)
class Node:

	def __init__(self, character, value):
		#nodes are characters in a trie
		self.character = character
		#like a dictionary: key (char) - value (integer) pairs
		self.value = value
		#every node may have several children - this is why tries are not memory-efficient
		#every node has 26 children no matter they are needed or not
		self.children = [None for _ in range(ALPHABET_SIZE)]
		#we have to track whether a given node is a leaf node or not 
		#leaf nodes are the end of given words in the tree
		self.leaf = False
		
class Trie:

	def __init__(self):
		#the root node is an empty node (here we use *)
		self.root = Node('*',None)
		
	#inserting an item takes O(M) time where M is the size of the key we insert
	def insert(self, key, value):
	
		#always start at the root node
		current = self.root

		#consider all the letters of the key
		for char in key:

			#we are dealing with indexes: use ASCII representation to get the index and transform
			#within the range [0,ALPHABET_SIZE-1]
			ascii_index = ord(char)-ord('a')				
		
			#there may be a child with the given letter
			if current.children[ascii_index]:
				#we keep going
				current = current.children[ascii_index]
			else:
				#otherwise we insert a new node with the given character
				node = Node(char,value)
				current.children[ascii_index] = node
				current = node

		#after we considered all the letters of the word ... it is the end of a word
		#leaf nodes represent end of words in the tree
		current.leaf = True
	
	#checks whether given word is present in the tree or not [running time is O(M)]
	def get(self, word):
	
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
				return None
	
		#if we've considered all the letters and the actual node is a leaf node: we found the word
		if current.leaf:
			return current.value

		#word is not present in the tree
		return None
		
if __name__ == "__main__":

	#a dictionary like this has O(M) running time [NO COLLISIONS!!!] so it is deterministic
	#tries support sorting operation (hashtables and dictionaries do not)
	#disadvantage: huge memory complexity (every node has 26 children even if not needed)
	trie = Trie()
	
	trie.insert('she',1)
	trie.insert('adam',2)
	trie.insert('kevin',3)
	trie.insert('adamma',4)
	trie.insert('shell',5)
	trie.insert('seashore',6)
	
	print(trie.get('computer'))