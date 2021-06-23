from linked_list import LinkedList

def merge_sort(l):

    if l.size()==1:
        return l
    elif l.head==None:
        return l

    if l.head==None or l==None:
        return l

    left_half, right_half = split(l)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(l):
    if l==None or l.head==None:
        return l, None
    else:
        size = l.size()
        mid = size// 2
        mid_node = l.node_at_index(mid - 1)

        left = l
        right = LinkedList()
        right.head = mid_node.next_node
        mid_node.next_node = None

        return left, right










l = LinkedList()

import  random
for i in range(10):
    for n in [random.randint(1,100)]:
        l.add(n)
print(l)
a = merge_sort(l)
print(a)
