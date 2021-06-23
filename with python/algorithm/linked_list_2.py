
class Node:

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __int__(self):
        return self.data

    def __str__(self):
        return f'{self.data}'
    # def __repr__(self):
        # return f'Node data:{self.data}'



class linked_list:

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        current = self.head
        nodes = 0

        while not current==None:
            nodes += 1
            current = current.next_node

        return nodes

    def __repr__(self):
        current = self.head
        nodes = []
        while current!=None:
            nodes.append(str(current.data))
            current = current.next_node
        return '-> '.join(nodes)

    def search(self, key):
        current = self.head

        while current:
            if current.data==key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, index, data):
        if index==0:
            self.add(data)

        new = Node(data)
        current = self.head
        position = index

        while position > 1 :
            current = current.next_node
            position -= 1

        prev = current
        next = current.next_node

        prev.next_node = new
        new.next_node = next




    def remove(self, key):

        current = self.head
        prev_current = current

        while current:
            if current.data==key and current==self.head:
                self.head = current.next_node

            elif current.data==key:
                prev_current.next_node = current.next_node
                return True

            else:
                prev_current = current
                current = current.next_node

        return False



# a = linked_list()
# a.add(11)
# a.add(10)
# a.add(9)
# a.add(12)
# a.add(2478)
# a.add(2546)
# a.add(4567)
# print(a)
# print(a.size())
# print(a.search(9))
# print(a.insert(3, 18))
# print(a)
# print(a.remove(4567))
# print(a)