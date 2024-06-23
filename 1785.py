"""
You are given an integer array nums and two integers limit and goal. The array nums has an interesting property that abs(nums[i]) <= limit.

Return the minimum number of elements you need to add to make the sum of the array equal to goal. The array must maintain its property that abs(nums[i]) <= limit.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: nums = [1,-1,1], limit = 3, goal = -4
Output: 2
Explanation: You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.
Example 2:

Input: nums = [1,-10,9,1], limit = 100, goal = 0
Output: 1
 

Constraints:

1 <= nums.length <= 105
1 <= limit <= 106
-limit <= nums[i] <= limit
-109 <= goal <= 109
"""


from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:

		# Calculate current sum and how far we are from goal
        current_val = sum(nums)
        abs_difference = abs(goal - current_val)

		# Calculate new limits as , we will never be adding  / subtracting numbers </> abs_difference
        limit = min(abs_difference,limit)
        maximize = True
		
        if current_val <= goal:
            possible_additions = list(range(0,limit+1))
            print(nums)
            print("Current Value := ",current_val)
            print("Goal := ",goal)
            print("We need to add values := ",abs_difference)
            print("Possible Values := ",possible_additions)

        else:
            maximize = False
            possible_additions = list(range(-limit,0))
            print("Current Value := ",current_val)
            print("Goal := ",goal)
            print("We need to subtract values := ",abs_difference)
            print("Possible Values := ",possible_additions)
        
        counts = 0
        if maximize:
            start = len(possible_additions) - 1
            while abs_difference != 0 and start > -1:
				# We can easily calculate quotient as max additions per element
                max_additions = abs_difference // possible_additions[start]
                if max_additions:
                    print(f"Add {possible_additions[start]} , {max_additions} time(s).")
                    abs_difference -= possible_additions[start] * max_additions
                    counts += max_additions
                else:
                    start -= 1
        else:
            start = 0
            while abs_difference != 0 and start < len(possible_additions):
				# We can easily calculate quotient as max additions per element
                max_additions = abs_difference // abs(possible_additions[start])
                if max_additions:
                    print(f"Subtract {possible_additions[start]} , {max_additions} time(s).")
                    abs_difference += possible_additions[start] * max_additions
                    counts += max_additions
                else:
                    start += 1

        print("\n=======================\n")



        return counts
