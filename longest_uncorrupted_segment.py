def longestUncorruptedSegment(sourceArray, destinationArray):
    curr, maxx, curr_i, maxx_i = 0, 0, 0, 0

    for j, (s, d) in enumerate(zip(sourceArray, destinationArray)):
        if s == d:
            if curr == 0:
                curr_i = j
            curr += 1

        if s != d or j == len(sourceArray) - 1:
            if curr > maxx:
                maxx = curr
                maxx_i = curr_i
            curr = 0

    return [maxx, maxx_i]


print(longestUncorruptedSegment([33531593, 96933415, 28506400, 39457872, 29684716, 86010806], [
      33531593, 96913415, 28506400, 39457872, 29684716, 86010806]))
