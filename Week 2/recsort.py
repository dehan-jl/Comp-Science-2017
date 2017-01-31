def recsort(i, ll, list0):
    if len(list0) == 0:
        return list0
    list2[i] = min(list0)
    list2[ll - i - 1] = max(list0)
    del list0[list0.index(min(list0))]
    del list0[list0.index(max(list0))]
    print(list0)
    print(list2)
    i += 1
    print(i)
    recsort(i, ll, list0)


list1 = [18, 12, 13, 8, 7, 16, 14]
ll = len(list1)
list2 = [None] * ll
if len(list1) % 2 != 0:
    list1.append(0)
recsort(0, ll, list1)