# return True if a contiguous subarray equal to s exists
""" def csubarray_equal_to_s_exists(s, arr):
    for i in range(0, len(arr)):
        result = arr[i]
        j = i

        while result < s:
            j += 1
            if j == len(arr):
                break
            result += arr[j]
            if result == s:
                return True

    return False """


# print(csubarray_equal_to_s_exists(12, [1, 2, 3, 7, 5]))


# return True if a contiguous subarray equal to s exists
# More efficient sliding window approach
""" def sliding_window_approach(s, arr):
    window = []

    for x in arr:
        window.append(x)

        if sum(window) > s:
            window.pop(0)

        if sum(window) == s:
            return True
    return False


print(sliding_window_approach(16, [1, 2, 3, 7, 5]))
 """

# Returns the start and end indexes (in 1-based form)
# of the window in which the sum was found. If the sum
# is not found returns [-1]

"""
def sliding_window_approach2(s, arr):
    window = []

    for i, x in enumerate(arr):
        window.append((x, i))

        if sum(e[0] for e in window) > s:
            window.pop(0)

        if sum(e[0] for e in window) == s and window:
            return [window[0][1]+1, window[-1][1]+1]
    return [-1] """


def findLongestSubarrayBySum(s, arr):
    window = []
    curr_window = []

    for i, x in enumerate(arr):
        window.append((x, i))
        summ = sum(e[0] for e in window)
        if summ > s:
            while summ > s and window:
                window.pop(0)
                summ = sum(e[0] for e in window)

        if summ == s and len(window) > len(curr_window):
            curr_window = window[:]

    if not curr_window:
        return [-1]
    else:
        return [curr_window[0][1]+1, curr_window[-1][1]+1]


print(findLongestSubarrayBySum(12, [1, 2, 3, 7, 5]))

""" print(findLongestSubarrayBySum(468, [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37,
                                     192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 0, 172, 0, 139, 0, 0, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]))
 """



"""  def findLongestSubarrayBySum(s, arr):
    window = []
    curr_window = []
    prev_sum = 0
    for i, x in enumerate(arr):
        window.append((x, i))
        summ = prev_sum + x
        if summ > s:
            while summ > s and window:
                y = window.pop(0)
                summ -= y[0]

        prev_sum = summ

        if summ == s and len(window) > len(curr_window):
            curr_window = window[:]

    if not curr_window:
        return [-1]
    else:
        return [curr_window[0][1]+1, curr_window[-1][1]+1] """