
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
        # like a dictionary: key (char) - value (integer) pairs
        self.value = None


class Trie:

    def __init__(self):
        # the root node is an empty node (here we use *)
        self.root = Node('*')

    # inserting an item takes O(M) time where M is the size of the word we insert
    def insert(self, key, value):

        # always start at the root node
        current = self.root

        # consider all the letters of the word
        for char in key:
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
        current.value = value

    # checks whether given word is present in the tree or not [running time is O(M)]
    def get(self, key):

        # if the tree is empty we return false
        if not self.root.children:
            return False

        # always start with the root node
        current = self.root

        # consider all the letters of the word
        for char in key:
            # we are dealing with indexes: use ASCII representation to get the index and transform
            # within the range [0,ALPHABET_SIZE-1]
            ascii_index = ord(char) - ord('a')

            # the given letter is present in the tree (so there is a valid child)
            if current.children[ascii_index]:
                # keep going and consider that given node
                current = current.children[ascii_index]
            else:
                # otherwise we know the key is not present in the tree
                return None

        # if we've considered all the letters and the actual node is a leaf node: we found the word
        if current.leaf:
            return current.value

        return None


if __name__ == '__main__':

    trie = Trie()

    trie.insert('adam', 10)
    trie.insert('car', 2)
    trie.insert('bus', 6)
    trie.insert('computer', 20)

    print(trie.get('car'))



