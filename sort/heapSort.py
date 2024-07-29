from typing import List

def heapify(lis, n, i) -> None:
    large = i
    l = 2*i + 1
    r = 2*i + 2
    
    if l < n and lis[l] > lis[large]:
        large = l
    if r < n and lis[r] > lis[large]:
        large = r
    if large != i:
        lis[large], lis[i] = lis[i], lis[large]
        heapify(lis, n, large)


def sort(lis) -> None:
    le = len(lis)
    for i in range(le//2 - 1, -1, -1):
        heapify(lis, le, i)
    for i in range(le-1, -1, -1):
        lis[i], lis[0] = lis[0], lis[i]
        heapify(lis, i, 0)

lis = [10, 7, 1, 3, 2, 5, 11]
sort(lis)
print(lis)