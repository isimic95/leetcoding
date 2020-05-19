def lineUp(commands):
    same_count = 0
    turning_the_same = True

    for command in commands:
        if turning_the_same and command == "A":
            same_count += 1
        elif turning_the_same and command in ("R", "L"):
            turning_the_same = False
        elif not turning_the_same and command in ("R", "L"):
            turning_the_same = True
            same_count += 1
    return same_count


print(lineUp("LLARL"))


""" if prev == "":
            prev = command
        else:
            prev += command
            if prev in same_dir_combs:
                same_count += 1
                prev = "" """
