def convert_to_output(l):
    d = {x: x for x in l}
    seen = []
    segments = []
    for x in l:
        if x not in seen:
            seen.append(x)
            segment = []
            y = x
            while y+1 in d.keys():
                y += 1
                seen.append(y)

            segment = [x, y]
            segments.append(segment)
    return segments


print(convert_to_output([2, 3, 4, 6, 8, 9, 10]))
# dok je iduci
""" def blockStorageRewrites(blockCount, writes, threshold):
    num_of_writes = {}

    for write in writes:
        for block in range(write[0], write[1]+1):
            try:
                if num_of_writes[block] < threshold:
                    # block_storage.append(block)
                    # if len(block_storage) == blockCount:
                    #    break
                    num_of_writes[block] += 1
            except KeyError:
                num_of_writes[block] = 1

    return_list = []
    for k, v in num_of_writes.items():
        if v == threshold:
            return_list.append(k)
    return_list = sorted(return_list)

    return convert_to_output(return_list)


print(blockStorageRewrites(10, [[0, 4], [3, 5], [2, 6]], 2)) """
