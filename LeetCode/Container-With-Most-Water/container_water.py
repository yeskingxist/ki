def maxArea(height):
    max_val = 0
    l = 0
    r = len(height) - 1
    while l < r:
        width = r - l
        max_val = max(max_val, min(height[l], height[r]) * width)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_val
