def hamming_distance(x, y):
    return sum(int(x) for x in bin(x ^ y)[2:])


print(hamming_distance(1, 4))
