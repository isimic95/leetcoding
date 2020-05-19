def innerRanges(nums, l, r):
    result = []
    for i,num in enumerate(nums):
        if i+1<len(nums)-1 and num - nums[i+1] == 1:
            result.append(str(num+1))
        elif i == len(num) - 1:
            result.append(str(num) + "->" + "r")
        else:
            result.append(str(num-1) + "->" + str(nums[i+1]-1))
    return result