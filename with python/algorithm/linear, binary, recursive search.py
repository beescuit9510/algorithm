''''''
'''Linear Search'''
''''''
def linear_search(list, target):
    for i, item in enumerate(list):
        if target==item:
            return i
    return None

def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i]==target:
            return i
    return None




def verify(index):
    if index is not None:
        print(f"Target Found at index: {index}")
    else:
        print("Target not found in list")


numbers = [n for n in range(-11,11)]

'''check if everything works as expected'''
'''if each one of them produces unexpected result, then the algorithm is not working'''

# r = linear_search(numbers, 6)
# verify(r)
#
# r = linear_search(numbers, 12)
# verify(r)








''''''
'''Binary Search'''
''''''

'''run on constant space'''

def Binary_seach(list, target):
    first = 0
    last = len(list)-1
    while first <= last:
        midpoint = (first+last)//2
        if list[midpoint]==target:
            return midpoint
        elif list[midpoint]<target:
            first = midpoint+1
        else:
            last = midpoint-1
    return None


# r = Binary_seach(numbers, 6)
# verify(r)










'''
recursive_binary_search
'''

'''
while swift is recursion-familiar,
python is not(limited), so when run recursive implementation
it requires much memory than binary(iterative implementation)
choose iterative one(in python), when the other conditions are same
'''

def recursive_binary_search(list, target):
    if len(list)==0:
        return False
    midpoint = len(list)//2
    if list[midpoint]==target:
        return True
        # return list[midpoint]
    else:
        if list[midpoint]<target:
            return recursive_binary_search(list[midpoint+1:], target)
        else:
            return recursive_binary_search(list[:midpoint], target)

def verify(r):
    print(f"Target found: {r}")

# verify(recursive_binary_search(numbers, 1))




