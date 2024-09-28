                                -------------AGGRESIVE COWS---------------------

We have several stalls, each located at a certain position on a straight line. We want to place a number of cows in these stalls,
but we want to maximize the minimum distance between any two cows. The goal is to figure out what that largest minimum distance can be.

Example:
Suppose we have the following stall positions and cows:

stalls = [1, 2, 8, 4, 9]
cows = 3
We want to place 3 cows in such a way that the minimum distance between any two cows is as large as possible.

Step-by-Step Explanation of the Code:

=>1. Sorting the Stall Positions:
Since the cows can only be placed in stalls that are further apart, we need to sort the stall positions first.
This helps us easily calculate distances between consecutive stalls.

stalls = [1, 2, 8, 4, 9]
stalls.sort()  # Sorted stall positions: [1, 2, 4, 8, 9]

=>2. Using Binary Search to Find the Largest Minimum Distance:
We don’t know what the largest minimum distance should be, so we use binary search to test different values for the minimum distance.
Binary search is efficient because it narrows down the possible range by half at each step.

We initialize low to 1 (the smallest possible distance between two cows).
We initialize high to the difference between the first and last stall, which is high = stalls[-1] - stalls[0] = 9 - 1 = 8.
So, initially:

low = 1
high = 8

=>3. Testing Midpoint Distance:
In each iteration of binary search, we calculate the midpoint distance as (low + high) // 2 and check if we can place all the cows
with at least this distance between them.

First iteration:
mid = (1 + 8) // 2 = 4
We now check if it's possible to place all 3 cows such that the distance between them is at least 4 units apart.

=>4. Checking if We Can Place the Cows (canPlaceCows function):
This function tries to place the cows in the stalls while ensuring that the distance between any two cows is at least minDist.

For the first iteration (minDist = 4):

Start by placing the first cow in the first stall at position 1.

lastPos = 1  # First cow is placed in the first stall
count = 1  # We've placed 1 cow so far
Now, try to place the next cows in stalls such that they are at least 4 units apart:

Check stall 2 (position 2). The distance from the last placed cow (position 1) is 2 - 1 = 1, which is less than 4, so we skip this stall.

Check stall 3 (position 4). The distance from the last placed cow (position 1) is 4 - 1 = 3, which is less than 4, so we skip this one too.

Check stall 4 (position 8). The distance from the last placed cow (position 1) is 8 - 1 = 7, which is greater than 4, so we place the second cow here.

lastPos = 8  # Second cow placed in stall at position 8
count = 2  # We've placed 2 cows so far
Check stall 5 (position 9). The distance from the last placed cow (position 8) is 9 - 8 = 1, which is less than 4, so we cannot place a cow here.

We couldn't place the third cow with a minimum distance of 4, so canPlaceCows returns False.

=>5. Updating the Binary Search:
Since it wasn’t possible to place all cows with at least 4 units apart, we need to try smaller distances. We adjust the high value to mid - 1 = 4 - 1 = 3.

New range for binary search:

low = 1
high = 3
=>6. Second Iteration:
In the second iteration, the new mid value is (1 + 3) // 2 = 2. Now, we check if it’s possible to place the cows with at least 2 units apart.

Start by placing the first cow in the first stall at position 1.
Place the second cow in stall 3 (position 4), since 4 - 1 = 3 (greater than 2).
Place the third cow in stall 4 (position 8), since 8 - 4 = 4 (greater than 2).
Since we successfully placed all cows with at least 2 units apart, canPlaceCows returns True.

=>7. Update the Result and Continue:
Since it’s possible to place the cows with a distance of 2, we store this as the current largest minimum distance and try for larger distances by updating low to mid + 1 = 2 + 1 = 3.

New range for binary search:

low = 3
high = 3
8. Third Iteration:
In the third iteration, mid = (3 + 3) // 2 = 3. Now we check if we can place the cows with at least 3 units apart.

Start by placing the first cow in the first stall at position 1.
Place the second cow in stall 3 (position 4), since 4 - 1 = 3 (equal to 3).
Place the third cow in stall 4 (position 8), since 8 - 4 = 4 (greater than 3).
Since we successfully placed all cows with a distance of 3, canPlaceCows returns True.

=>9. Final Adjustment:
Since it’s possible to place the cows with 3 units apart, we update res = 3 and try for larger distances by setting low = mid + 1 = 3 + 1 = 4.

Now, low > high (4 > 3), so the binary search terminates.

Final Result:
The largest minimum distance where we can place the cows is 3. This is the answer.

print(f"The largest minimum distance is: {result}")
Output:The largest minimum distance is: 3

---Summary of Code Flow---
Sort the stalls.
Use binary search to check different minimum distances (mid) and try to place the cows using the canPlaceCows function.
Adjust the binary search range based on whether we can place the cows with the current mid distance.
Repeat until binary search terminates, and the result will be the largest possible minimum distance.
