def binary_search(target, li):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if target == li[mid]:
            return mid
        elif target < li[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return -1


ll = [1,2,3,4,5,6,7,8,9]

print(binary_search(7, ll))
