def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0  
    while left < right:
        width = right - left
        height_of_container = min(height[left], height[right])
        current_area = width * height_of_container
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1  
        else:
            right -= 1 
    return max_area
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height1))  
height2 = [1, 1]
print(maxArea(height2)) 
