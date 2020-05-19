#brute force
def maxArea(height) -> int:
    maxArea = 0
    j = len(height) - 1

    while j > 0:
        for i, x in enumerate(height):
            if x > height[j]:
                y = height[j]
            else:
                y = x

            currArea = y*(j-i)
            maxArea = max(currArea, maxArea)

        j -= 1
    return maxArea


#smarter
def maxArea(height):        
        i = 0
        j = len(height) - 1
        max_area = 0
        while i != j:
            if height[i] <= height[j]:
                max_area = max(max_area, (j - i) * height[i])
                i += 1
            else:
                max_area = max(max_area, (j - i) * height[j])
                j -= 1
                
        return max_area


print(maxArea([1, 1]))
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
