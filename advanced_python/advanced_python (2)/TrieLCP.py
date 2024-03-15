ALPHABET_SIZE = 128


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
        self.lcp_index = 0

    # it has the running time of O(M) where M is the longest string in the trie
    def lcp(self):

        node = self.root
        s = ''

        while self.count_children(node) == 1 and not node.leaf:
            node = node.children[self.lcp_index]
            s = s + chr(self.lcp_index)

        return s

    def count_children(self, node):

        n = 0

        for i, child in enumerate(node.children):
            if child is not None:
                n = n + 1
                self.lcp_index = i

        return n

    # inserting an item takes O(M) time where M is the size of the word we insert
    def insert(self, word):

        # always start at the root node
        current = self.root

        # consider all the letters of the word
        for char in word:
            # we are dealing with indexes: use ASCII representation to get the index and transform
            # within the range [0,ALPHABET_SIZE-1]
            ascii_index = ord(char)

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
            ascii_index = ord(char)

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
    trie.insert('128.354.321.675')
    trie.insert('128.354.721.143')
    trie.insert('128.354.351.034')
    trie.insert('128.354.221.654')

    print(trie.lcp())
