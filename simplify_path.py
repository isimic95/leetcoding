def simplifyPath(path):
    while '//' in path:
        path = path.replace('//', '/')
    dirs = []

    for dir in path.split('/'):
        if dir == '..':
            if dirs[-1] != '':
                dirs.pop()
        elif dir != '.':
            dirs.append(dir)

    print(dirs)
    result = ("/" + "/".join(dirs)).rstrip("/").replace("//", "/")
    if result == '':
        result = '/'
    return result


print(simplifyPath("/home/../../.."))
print(simplifyPath("/home/"))
print(simplifyPath("/../"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/a/./b/../../c/"))
print(simplifyPath("/a/../../b/../c//.//"))
print(simplifyPath("/a//b////c/d//././/.."))