# capacity of the cache (how many items it can store)
CAPACITY = 4


# node in the doubly linked list
class Node:

    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.previous_node = None
        self.next_node = None


class DoublyLinkedList:

    # update the first and last items in O(1)
    def __init__(self):
        self.head = None
        self.tail = None


class LRUCache:

    def __init__(self):
        self.actual_size = 0
        # we store integer node id - Node pairs: this is how we can find a node in O(1)
        self.dictionary = {}
        self.linked_list = DoublyLinkedList()

    # data can be a website
    def put(self, id, data):

        # update the node if already exists (we have to check whether the dict is empty first)
        if id in self.dictionary:
            node = self.dictionary[id]
            node.data = data
            # update the node to be the head (cache feature)
            self.update(node)
            return

        # the data is not present in the cache so insert
        node = Node(id, data)

        # we have to insert into the cache + set it to be the head node
        if self.actual_size < CAPACITY:
            self.actual_size = self.actual_size + 1
            self.add(node)
        else:
            # the cache is full: we have to remove the last item + insert the new one
            self.remove_tail()
            self.add(node)

    # add node to the head of the doubly linked list
    def add(self, node):

        # the node will be the new head: so update accordingly
        node.next_node = self.linked_list.head
        # it is the first node: no previous node
        node.previous_node = None

        # we have to update the previous head: point to the new head (which is the node)
        if self.linked_list.head:
            self.linked_list.head.previous_node = node

        # update the head node
        self.linked_list.head = node

        # if there is 1 node in the list: it is the head as well as the tail
        if not self.linked_list.tail:
            self.linked_list.tail = node

        # we have to update the dictionary with the node !!!
        self.dictionary[node.id] = node

    # remove last item (least frequently used)
    def remove_tail(self):

        # get node from the dictionary O(1)
        last_node = self.dictionary[self.linked_list.tail.id]

        # remove the node from the dictionary
        del self.dictionary[self.linked_list.tail.id]

        # new tail node is the previous node (because we remove the actual one)
        self.linked_list.tail = self.linked_list.tail.previous_node

        # set the next node to be a NULL: because it is the right-most item
        if self.linked_list.tail:
            self.linked_list.tail.next_node = None

        last_node = None

    # get the item with ID id + move to the head because we've visited this item
    def get(self, id):

        # the dictionary does not contain the item [O(1) running time!!!]
        if not self.dictionary[id]:
            return None

        # the dictionary contains the item
        node = self.dictionary[id]
        # move to the head (frequently visited items must be close to the head)
        self.update(node)

        return node

    # move the given node to the front (head)
    def update(self, node):

        # doubly linked list: we can get the previous node and the next node
        previous_node = node.previous_node
        next_node = node.next_node

        # so it is a middle node (not the head) in the list
        if previous_node:
            previous_node.next_node = next_node
        else:  # we know that this is the head (first node)
            self.linked_list.head = next_node

        # so not the last node
        if next_node:
            next_node.previous_node = previous_node
        else:  # we know it is the last node
            self.linked_list.tail = previous_node

        # we have to move the node to the front
        self.add(node)

    def show(self):

        actual_node = self.linked_list.head

        # consider all the nodes in the linked list
        while actual_node:
            print("%s->" % actual_node.data)
            actual_node = actual_node.next_node


if __name__ == '__main__':

    cache = LRUCache()

    cache.put(0, 'www.google.com')
    cache.put(1, 'www.facebook.com')
    cache.put(2, 'www.globalsoftwaresupport.com')
    cache.put(3, 'www.udemy.com')
    cache.put(4, 'www.linkedin.com')

    cache.show()
    print('\n' + cache.get(3).data + '\n')

    cache.show()
    print('\n' + cache.get(2).data + '\n')
    cache.show()

    cache.put(5, 'www.programming.com')
    cache.show()


