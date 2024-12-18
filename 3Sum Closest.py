def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf') 
    for i in range(len(nums) - 2):  
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return current_sum
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1 
            else:
                right -= 1 
    return closest_sum
nums1 = [-1, 2, 1, -4]
target1 = 1
print(threeSumClosest(nums1, target1))
nums2 = [0, 0, 0]
target2 = 1
print(threeSumClosest(nums2, target2))

