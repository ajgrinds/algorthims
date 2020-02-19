import itertools


def combinations(n1, n2, max_len):
    ans = [set(itertools.combinations(range(n1 + n2), i)) - set(itertools.combinations(range(n1), i)) -
           set(itertools.combinations(range(n1, n1 + n2), i)) for i in range(2, max_len + 1)]
    final = []
    for x in ans:
        for z in x:
            final.append(z)
    return final
