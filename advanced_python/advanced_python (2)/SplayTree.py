
class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_node = None
        self.right_node = None


class SplayTree:

    def __init__(self):
        self.root = None

    # it is exactly the same as BST
    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    # BST insertion
    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

    # find a given arbitrary item in the BST
    def find(self, data):

        node = self.root

        while node is not None:
            if data < node.data:
                node = node.left_node
            elif data > node.data:
                node = node.right_node
            else:
                self.splay(node)
                return node.data

    def splay(self, node):

        # while we hit the root node - this is how we make the node
        # to be the root node (caches)
        while node.parent is not None:
            # the node is a left or right child of the root
            # CASE 3 - ZIG SITUATION
            if node.parent.parent is None:
                if node == node.parent.left_node:
                    self.rotate_right(node.parent)
                else:
                    self.rotate_left(node.parent)
            # doubly left heavy case ZIG-ZIG SITUATION
            elif node == node.parent.left_node and node.parent == node.parent.parent.left_node:
                self.rotate_right(node.parent.parent)
                self.rotate_right(node.parent)
            elif node == node.parent.right_node and node.parent == node.parent.parent.right_node:
                self.rotate_left(node.parent.parent)
                self.rotate_left(node.parent)
            # ZIG-ZAG SITUATIONS
            elif node == node.parent.left_node and node.parent == node.parent.parent.right_node:
                self.rotate_right(node.parent)
                self.rotate_left(node.parent)
            else:
                self.rotate_left(node.parent)
                self.rotate_right(node.parent)

    def rotate_right(self, node):

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

    def rotate_left(self, node):

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node


if __name__ == '__main__':

    splay_tree = SplayTree()
    splay_tree.insert(10)
    splay_tree.insert(8)
    splay_tree.insert(3)
    splay_tree.insert(7)

    splay_tree.find(7)
    splay_tree.find(3)
    splay_tree.find(8)
    splay_tree.find(3)
    print(splay_tree.root.data)

