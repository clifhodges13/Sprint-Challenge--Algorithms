#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity is O(log n) because at each iteration of the while loop, we are increasing the value of a by n^2, getting us closer and closer to n^3, which is our termination point.


b) The runtime complexity is O(n log n) because we have a loop nested inside another loop, both of which would normally be O(n), but within the while loop we are doubling the value of j each time, bringing it closer to the termination point (n) much faster, at log n speed.


c) We're trying to get to our base case where bunnies is equal to 0. Each time bunnies is larger than 0, we recurse and subtract 1 from the value of bunnies. Therefore, this function's runtime is O(n). The number of steps is dependent on the input.

## Exercise II


- Building has n stories
- Plenty of eggs (implies we won't run out)
- Dropping eggs from floor F and above breaks eggs, below F does not
- Determine the value of F to minimize broken eggs
- We'll have dropped eggs and broken eggs. If an egg is dropped and broken, that means the floor it was dropped from is F or higher.
- If the egg is ONLY dropped and not broken, it was dropped from below floor F.

Define a function that takes number of floors
    create a list to hold all floors f and greater
    Loop through each floor n,
        Drop an egg,
        If it breaks,
            mark the floor as f or greater by adding it to the list above
        If it does not break,
            continue to the next floor
    Loop through the floors list and find the smallest value. This will be the value of F
    return F

__________
The runtime complexity of this function would be O(2n) because there are 2 iterations happening, one after the other.
