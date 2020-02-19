import itertools


def combinations(n1, n2, max_len):
    ans = [set(itertools.combinations(range(n1 + n2), i)) - set(itertools.combinations(range(n1), i)) -
           set(itertools.combinations(range(n1, n1 + n2), i)) for i in range(2, max_len + 1)]
    final = []
    for x in ans:
        for z in x:
            final.append(z)
    return final


def all_indexes(arr, symbol):
    indexes = []
    i = 0
    while i != len(arr):
        if arr[i] == symbol:
            indexes.append(i)
        i += 1
    return indexes
