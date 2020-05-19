def reverse_words(l):
    word = ""
    new_order = []
    for c in l:
        if c != ' ':
            word += c
        else:
            new_order.append(word)
            word = ""

    new_order.append(word)
    return " ".join(new_order[::-1])


message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']

print(reverse_words(message))

message = ['t', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ',
           'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd']

print(reverse_words(message))


""" def reverse_words(l):
    prev = 0
    new_order = []
    word = ""
    for i,c in enumerate(l):
        if c == ' ':
            word = "".join(l[prev:i])
            new_order.append(word)
            prev = i+1

    new_order.append(word)
    return " ".join(new_order[::-1]) """