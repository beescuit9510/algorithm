def merge_sort(list):
    '''
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes 0(n log n) time
    '''
    ##### Not like the actual merge_sort algorith,
    ##### in Python, Takes 0(kn log n) time with slicing operation, list[:mid]

    if len(list) <= 1:
        return list

    right_half, left_half = divide(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # for visual check
    # return left, left

    return merge(left, right)



def divide(list):
    '''
    Divide the unsorted list at midpoint into sublists
    Returns two sublists = left and right

    Takes overall 0(log n) (logarithmic time)
    ---> How the actually merge_sort algorithm works

    0(k log n)
    --->In Python, slicing operation takes k
    '''

    midpoint = len(list)//2
    right = list[:midpoint]
    left = list[midpoint:]



    return right, left



def merge(left, right):
    '''
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall 0(n) time(linear time)
    '''
    l = []
    i = 0
    j = 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while len(left) > i:
        l.append(left[i])
        i += 1

    while len(right) > j:
        l.append(right[j])
        j += 1

    return l




def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


# import  random
# alist = [n for n in range(1, 51, 10)]
# random.shuffle(alist)
#
# print(alist)
# l = merge_sort(alist)
# print(l)
# print(verify_sorted(l))

