class Node:
    '''
    An object for storing a single node of  a linked list.
    Models two attributes - data and the link to the next node in the list
    '''

    # data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"





class LinkedList:
    '''
    Singly linked list
    '''

    def __init__(self):
        self.head = None


    def is_empty(self):
        return self.head == None


    def size(self):
        '''
        Return the number of nodes in the list
        Takes O(n) time(linear time)
        '''
        current = self.head
        count = 0

        while current:
            current = current.next_node
            count += 1

        return count

    def add(self, data):
        '''
        Adds new Node containing data at head of the list
        Takes O(1) time(constant time)
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        '''
        Now, class Node __init__ stored in self.head
        '''

    def search(self, key):
        '''
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found

        Takes 0(n) time(linear time)
        '''
        current = self.head

        while current:
            if current.data==key:
                return current.data
            else:
                current = current.next_node
        return None


    def __repr__(self):
        '''
        return a string representaion of the list
        Take 0(n) time(linear time)
        '''
        current = self.head
        nodes = []

        while current is not None:
            if current==self.head:
                nodes.append(f'[Head: {current.data}]')
            elif current.next_node==None:
                nodes.append(f'[tail: {current.data}]')
            else:
                nodes.append(f'[{current.data}]')
            current = current.next_node

        return '-> '.join(nodes)


    def insert(self, index, data):
        '''
        Insert a new Node containing data at index position
        insertion takes 0(1) (constant time),
        but finding the node at the insertion point takes 0(n)(linear time).

        Therefore
        Takes overall 0(n) (linear time)
        '''


        if index==0:
            self.add(data)

        new = Node(data)
        position = index
        current = self.head
        while position > 1:
            current = current.next_node
            position -= 1

        prev = current
        prev_next = current.next_node

        prev.next_node = new
        new.next_node = prev_next


    def remove(self, key):
        '''
        Removes Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes 0(n) (linear time)
        '''

        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data==key and current==self.head:
                '''
                current.data indicates int
                current indicates itself(class)
                '''
                self.head = current.next_node
                found = True
            elif current.data==key:
                previous.next_node = current.next_node
                found = True
            else:
                previous = current
                current = current.next_node


    def node_at_index(self, index):
        if index ==0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position +=1
            return current







#
#
# l = LinkedList()
# l.add(5)
# l.add(10)
# l.add(5)
# print(l.size())
# print(l)
# print(l.search(10))
# l.insert(2, 20)
# print(l)
# l.remove(20)
# print(l)