def bubble_sort(li):
    n = len(li)
    for i in range(n):
        for j in range(n - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


ll = [4,1,8,3,9,2,6,7, 0]

bubble_sort(ll)

print(ll)

