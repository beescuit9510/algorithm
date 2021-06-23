# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

from linkedlist import LinkedList

def merge_sort(l):
    '''
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists untill one remains

    Returns a sorted linked list

    Runs in 0(kn log n)
    '''

    if l.size()==1:
        return l
    elif l.head==None:
        return l

    right_half, left_half = divide(l)
    right = merge_sort(right_half)
    left = merge_sort(left_half)

    return merge(left, right)


def divide(linked_list):
    '''
    Divide the unsorted list at midpoint into sublists
    Takes 0(k log n) time
    '''


    '''    
    linked_list can be None
    when we call def divide(), and pass a linked_list with a single node
    in the case, we will return None for the right list
    '''
    if linked_list==None or linked_list.head==None:
        return linked_list, None
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid - 1)
        '''
        mid-1, when we find mid, we used size(),
        in which we return the length of the linked list (counting starts from 1)
        But index starts from 0
        '''
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half




def merge(left, right):
    '''
    Runs in 0(n) (linaer time)
    '''

    merged = LinkedList()
    merged.add(0)
    current = merged.head

    left_head = left.head
    right_head = right.head

    while left_head or right_head:

        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node

        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node

        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node

    head = merged.head.next_node
    merged.head = head

    return merged




'''explantion'''
        # def merge(left, right):
#     '''
#     Merges two linked lists, sorting bt data in nodes
#     Returns a new, merged list
#     '''
#
#     '''create a new linked list that contains node from
#     merging left and right'''
#     merged = LinkedList()
#
#     '''Add a fake head that is discarded later'''
#     merged.add(0)
#
#     '''Set current to the head of the linked list'''
#     current = merged.head
#
#     '''Obtain head nodes from left and right linked lists'''
#     left_head = left.head
#     right_head = right.head
#
#
#     '''Iterate over left and right
#     until we reach tail nodes of either'''
#     while left_head or right_head:
#
#         '''If the head node of left is None, we're past the tail
#         Add the node from right to merged linked list'''
#         if left_head is None:
#             current.next_node = right_head
#             '''Call next on right to set loop condition to false'''
#             right_head = right_head.next_node
#
#         elif right_head is None:
#             current.next_node = left_head
#             left_head = left_head.next_node
#
#         else:
#             '''Not at either tail node
#             Obtain node data to perform comparison operation'''
#             left_data = left_head.data
#             right_data = right_head.data
#
#             '''If data on left is less than right, set current to left node'''
#             if left_data < right_data:
#                 current.next_node = left_head
#                 '''Move left head to next node'''
#                 left_head = left_head.next_node
#             else:
#                 current.next_node = right_head
#                 right_head = right_head.next_node
#
#         '''Move current to next_node'''
#         current = current.next_node
#
#     '''Discard fake head and set first merged node as head'''
#     head = merged.head.next_node
#     merged.head = head
#
#     return merged


'''try 1'''
# def merge(left, right):
#
#     merged = LinkedList()
#     merged.add(0)
#
#     l_head = left.head
#     r_head = right.head
#
#     while l_head or r_head:
#     # for n in range(3):
#         if l_head==None:
#             merged.add(r_head)
#             r_head = r_head.next_node
#         elif r_head==None:
#             merged.add(l_head)
#             l_head = l_head.next_node
#
#         else:
#             if l_head.data > r_head.data:
#                 merged.add(r_head)
#                 r_head = r_head.next_node
#             else:
#                 merged.add(l_head)
#                 l_head = l_head.next_node
#         merged.head = merged.next_node



l = LinkedList()

import  random
for i in range(10):
    for n in [random.randint(1,100)]:
        l.add(n)
print(l)
a = merge_sort(l)
print(a)