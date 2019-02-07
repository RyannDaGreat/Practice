from rp import *
def quicksort(l):
    if len(l)<=1:
        return l
    left=[]
    right=[]
    pivot=l.pop(random_index(l))
    while l:
        e=l.pop()
        if e<pivot:
            left.append(e)
        else:
            right.append(e)
    return quicksort(left)+[pivot]+quicksort(right)
l=[randint(100) for i in range(100)]
print(l)
ans=quicksort(l)
print(ans)
