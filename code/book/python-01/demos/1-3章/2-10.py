def select_sort_simple(li):
    new_li = []
    for i in range(len(li)):
        min_val = min(li)
        new_li.append(min_val)
        li.remove(min_val)

    return new_li


def select_sort(li):
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]

ll = [5,1,8,2,9,3,6,7]

select_sort(ll)
print(ll)



