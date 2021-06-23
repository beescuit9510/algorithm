# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)

import random
alist = [n for n in range(1, 11)]
random.shuffle(alist)



def bogo_sort(list):
    attempt = 0
    while is_sorted(list) is False:
        print(attempt)
        random.shuffle(list)
        attempt += 1
    return list
def is_sorted(list):

    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True
# print(bogo_sort(alist))



'''recursion'''
def sum(numbers):

    '''We need a base case that causes the recursion to stop'''
    if not numbers:
        return 0
    # print(f'Calling sum {numbers[1:]}')
    remaining_sum = sum(numbers[1:])
    # print(f'Call to sum{numbers}, returning {numbers[0]}+{remaining_sum}')
    return numbers[0] + remaining_sum
# print(sum(alist))











'''
selection:
O(1/2 n^2)
1/2 --->
[5,7,2,3] [1]
[5,7,3] [1,2]
[5,7] [1,2,3]
[7] [1,2,3,5]
[1,2,3,5,7] 


O(n^2)
 when length of a list(n) get larger and larger
constant like 1/2 becomes insignificant
 so we usually discard it'''
def selection_sort(values):
    sorted_list = []
    # print(f'{values}, {sorted_list}')
    for i in range(len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        # print(f'{values}, {sorted_list}')

    return sorted_list
def index_of_min(values):
    min_index = 0
    for i in range(len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index
# print(selection_sort(alist))



'''
quicksort: recursion,
O(n log n) with the best case
that the pivot was the exact middle value of the list

O(n^2) with the worst case
that you will choose the pivot that's the biggest value of the list,
so that you cannot sort the list

on average, quicksort performs close to the best case
'''
def quicksort(values):
    if len(values) <= 1:
        return values

    pivot = values[0]
    less_than = []
    greater_than = []

    for v in values[1:]:
        if v <= pivot:
            less_than.append(v)
        else:
            greater_than.append(v)

    # print(f'{less_than, pivot, greater_than}')
    '''Visually, can see that python sort the left list(less_than)'''
    return quicksort(less_than) + [pivot] + quicksort(greater_than)
# print(quicksort(alist))



'''
Merge_sort: recursion,
O(n log n)
'''
def merge_sort(values):
    if len(values) <=1:
        return values

    mid_index = len(values)//2
    left_half = merge_sort(values[:mid_index])
    right_half = merge_sort(values[mid_index:])
    # print(f'{left_half}, {right_half}')

    l = 0
    r = 0
    merged = []

    while l < len(left_half) and r < len(right_half):
        if left_half[l] < right_half[r]:
            merged.append(left_half[l])
            l += 1
        else:
            merged.append(right_half[r])
            r +=1

    '''merged.append(left_half[l:]
    Append the list itself, not add elements in the list to the list, merged
    '''
    merged += left_half[l:]
    merged += right_half[r:]

    return merged
# print(alist)
# print(merge_sort(alist))





'''
each sorting speed by selection_sort, quicksort, merge_sort
the longest
selection(as much as quick+merge) >>>>>>
merge_sort >>
quicksort

in a real world,
quicksort, even tho that merge_sort runs on O(n log n ) regardless of the best and worst case
Number of time as operation is performed gets larger and larger
showing merge_sort takes longer than quicksort
'''







names = ['jack', 'sam', 'byunduc', 'Usman', 'jake', 'ariana']
search_names = ['jake', 'sam']


'''linear search'''
def index_of_item(collection, target):
    for i, name in enumerate(collection):
        if name == target:
            return i
    return None
# for n in search_names:
#     index = index_of_item(names, n)
#     print(index)




'''sorting names'''
sorted_names = quicksort(names)
# for n in sorted_names:
#     print(n)



def binary_search(collection, target):
    first = 0
    last = len(collection)-1
    while first <= last:
        mid = (first+last)//2
        if collection[mid]==target:
            return mid
        elif collection[mid] < target:
            first = mid +1
        else:
            last = mid -1
    return None

# for n in search_names:
    # index = binary_search(sorted_names, n)
    # print(index)