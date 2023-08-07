**TwoSum**

<u>Problem statement</u>

Given a list of integers and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
give the best python code for this which have minimum run time and memory.

<u>Approach</u>

- Initialize an empty dictionary called num_indices to store the elements of the list nums as keys and their indices as values.

- Iterate through the list nums using the enumerate function, which provides both the index i and the element num in each iteration.

- Calculate the complement, which is the difference between the target and the current element num. The complement represents the value that, when added to the current element, would result in the target value.

- Check if the complement is present in the num_indices dictionary. If the complement is present, it means we have found a pair of numbers whose sum equals the target. In this case, we return a list containing the indices of the two numbers.

- If the complement is not present in the num_indices dictionary, it means we haven't encountered the corresponding number for the current element yet. So, we add the current element num as a key in the num_indices dictionary, with its index i as the value.

- Repeat steps 3 to 5 for each element in the list nums, until we find a pair of numbers whose sum equals the target, or
until we finish iterating through the entire list.

- If no solution is found (i.e., no pair of numbers whose sum equals the target), the function returns an empty list [] to indicate that there is no valid pair.