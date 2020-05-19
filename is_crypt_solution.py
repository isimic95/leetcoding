# A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between
# letters and digits, such that the given arithmetic equation consisting of letters holds true when
# the letters are converted to digits.

# You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of
# letters and digits, solution. The array crypt will contain three non-empty strings that follow
#  the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.

# If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the
# mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes,
# the answer is true. If it does not become a valid arithmetic solution, the answer is false.

# Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).


def isCryptSolution(crypt, solution):
    # maketrans is a static method on string class
    ttable = "".maketrans(dict(solution))
    numbers = []

    for word in crypt:
        tword = word.translate(ttable)

        if len(tword) > 1 and tword[0] == '0':
            return False

        numbers.append(int(tword))
    if numbers[0] + numbers[1] == numbers[2]:
        return True
    else:
        return False
