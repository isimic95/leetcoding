def canJump(nums):
    if len(nums) == 1:
        return True

    while len(nums) > 1:
        start = nums[0]
        last_index = len(nums)-1

        while start >= 0:

            if start == last_index:
                return True
            elif start > last_index:
                start -= 1
            else:
                i = 1
                while nums[i] == 0:
                    nums = nums[i:]

                break
    return False


print(canJump([1, 1, 1, 0, 5]))
