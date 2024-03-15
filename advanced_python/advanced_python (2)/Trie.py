
ALPHABET_SIZE = 26


# the node in the tree structure (a node may contain given value - like a dictionary)
class Node:

    def __init__(self, character):
        # nodes are characters in a trie
        self.character = character
        # every node may have several children - this is why tries are not memory-efficient
        # every node has 26 children no matter they are needed or not
        self.children = [None for _ in range(ALPHABET_SIZE)]
        # we have to track whether a given node is a leaf node or not
        # leaf nodes are the end of given words in the tree
        self.leaf = False


class Trie:

    def __init__(self):
        # the root node is an empty node (here we use *)
        self.root = Node('*')

    # inserting an item takes O(M) time where M is the size of the word we insert
    def insert(self, word):

        # always start at the root node
        current = self.root

        # consider all the letters of the word
        for char in word:
            # we are dealing with indexes: use ASCII representation to get the index and transform
            # within the range [0,ALPHABET_SIZE-1]
            ascii_index = ord(char) - ord('a')

            if current.children[ascii_index] is not None:
                # keep going without creating a new node
                current = current.children[ascii_index]
            else:
                # otherwise we insert a new node with the given character
                node = Node(char)
                current.children[ascii_index] = node
                current = node

        # after we considered all the letters of the word ... it is the end of a word
        # leaf nodes represent end of words in the tree
        current.leaf = True

    def sort(self):
        return self.get_words_prefix('')

    def get_words_prefix(self, prefix):

        node = self.root
        # we store the words in a list
        words = []

        # we consider all the letters in the prefix
        for char in prefix:
            ascii_index = ord(char) - ord('a')

            # if there is no solution (for example words: [flower,flow,flight] and prefix is 'adam')
            if node.children[ascii_index] is None:
                return None

            node = node.children[ascii_index]

        # then we collect all the words starting with the same prefix
        self.collect(node, prefix, words)

        return words

    # depth-first search starting with the last node of the prefix
    def collect(self, node, prefix, words):

        # recursive implementation so this is the base case
        if node is None:
            return

        # leaf nodes represent valid words so we put them into the list
        if node.leaf:
            # node we keep appending letters to the prefix (so this prefix is
            # not the original prefix any more)
            words.append(prefix)

        # keep going and consider the next layers
        for child in node.children:
            # if the child is None we consider the next child (on the same level)
            if child is None:
                continue

            # we keep going down ... append the next letter to the prefix and
            # call the function recursively
            child_character = child.character

            self.collect(child, prefix+child_character, words)

    # checks whether given word is present in the tree or not [running time is O(M)]
    def find(self, word):

        # if the tree is empty we return false
        if not self.root.children:
            return False

        # always start with the root node
        current = self.root

        # consider all the letters of the word
        for char in word:
            # we are dealing with indexes: use ASCII representation to get the index and transform
            # within the range [0,ALPHABET_SIZE-1]
            ascii_index = ord(char) - ord('a')

            # the given letter is present in the tree (so there is a valid child)
            if current.children[ascii_index]:
                # keep going and consider that given node
                current = current.children[ascii_index]
            else:
                # otherwise we know the word is not present in the tree
                return False

        # if we've considered all the letters and the actual node is a leaf node: we found the word
        if current.leaf:
            return True

        return False


if __name__ == '__main__':

    trie = Trie()
    trie.insert('sea')
    trie.insert('seashell')
    trie.insert('shell')
    trie.insert('computer')
    trie.insert('science')
    trie.insert('house')
    trie.insert('electronics')

    print(trie.sort())










