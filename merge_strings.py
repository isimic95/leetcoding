from collections import Counter


def mergeStrings(s1, s2):
    cs1, cs2 = Counter(s1), Counter(s2)
    merged = []
    i, j = 0, 0

    while True:
        if i == len(s1):
            merged += list(s2[j:])
            break
        if j == len(s2):
            merged += list(s1[i:])
            break

        if cs1[s1[i]] < cs2[s2[j]]:
            merged.append(s1[i])
            i += 1
        elif cs1[s1[i]] == cs2[s2[j]]:
            if s2[j] < s1[i]:
                merged.append(s2[j])
                j += 1
            else:
                merged.append(s1[i])
                i += 1
        else:
            merged.append(s2[j])
            j += 1
    return "".join(merged)


print(mergeStrings("dce", "cccbd"))
