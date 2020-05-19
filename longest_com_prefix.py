def longestCommonPrefix(strs) -> str:
    if len(strs) == 0 or "" in strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]

    strs.sort(key=len)
    pref = ""
    prev = ""
    ind = 0
    flag = False

    while not flag:
        for i, s in enumerate(strs):
            if i == 0 and len(s) > ind:
                prev = s[ind]
                pref += s[ind]
            elif len(s) > ind and s[ind] == prev:
                continue
            else:
                pref = pref[:-1]
                flag = True
                break
        ind += 1

    return pref


print(longestCommonPrefix(["flower", "flow", "flight"]))
