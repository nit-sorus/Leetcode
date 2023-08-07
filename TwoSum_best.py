def two_sum(nums, target):
    # Create a dictionary to store elements and their indices
    num_indices = {}

    for i, num in enumerate(nums):
        # Calculate the complement (target - current number)
        complement = target - num

        # Check if the complement is present in the dictionary
        if complement in num_indices:
            # If found, return the indices of the two numbers
            return [num_indices[complement], i]

        # If not found, add the current number to the dictionary with its index
        num_indices[num] = i

    # If no solution is found, return an empty list
    return []


# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
