# 1480 - Running Sum of 1d Array (Easy)

# Time Complexity: O(n)
# Space Complexity: O(1)

def runningSum(nums):
    for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
    return nums


print(runningSum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]