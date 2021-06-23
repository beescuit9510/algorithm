def merge_sort(list):

    if len(list)<=1:
        return list

    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)

def merge(left, right):
    l = 0
    r = 0
    merged = []
    while len(left) > l and len(right) > r:
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    while len(left) > l:
        merged.append(left[l])
        l += 1

    while len(right) > r:
        merged.append(right[r])
        r += 1

    return merged




import random

l = []
for n in range(10):
    for n in[random.randint(5, 100)]:
        l.append(n)

print(l)
n = merge_sort(l)
print(n)