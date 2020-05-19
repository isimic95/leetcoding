def permute(nums):
    l = []

    if len(nums) == 0:
        return []

    if len(nums) == 1:
        return [nums]

    for i in range(len(nums)):
        m = nums[i]
        for p in permute(nums[:i] + nums[i+1:]):
            l.append([m] + p)
    return l


def yield_permute(nums):
    l = []

    if len(nums) == 0:
        yield []

    if len(nums) == 1:
        yield [nums]

    for i in range(len(nums)):
        m = nums[i]
        for p in permute(nums[:i] + nums[i+1:]):
            yield [m] + p


print(list(yield_permute([1, 2, 3])))
