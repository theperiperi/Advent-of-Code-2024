# Day 6: Part 2 - [Problem Name]

## Problem Description
In this part, the goal was to extend the logic to find a different condition within the character sequence. The new condition typically involves a longer unique sequence.

## Approach
To tackle this problem, I followed these steps:
1. **Reuse Previous Logic**: I reused the sliding window logic from Part 1 to maintain consistency.
2. **Adjust Window Size**: I modified the size of the sliding window to accommodate the new condition, allowing for the examination of longer substrings.
3. **Condition Checking**: I applied the same condition checking logic to the new window size, ensuring that the substring met the specified criteria.
4. **Output**: Finally, I printed the position where the new condition was first met.

This approach efficiently identifies the position for the new condition while building on the existing logic.

## Key Insights
- Reusing code can save time and reduce errors.
- Clear documentation of conditions is essential for maintaining code clarity.

## Concepts and Algorithms Used
- **Input Handling**: Reading from files and processing strings.
- **Data Structures**: Strings for character sequences.
- **Algorithms**: Sliding window technique for condition checking with adjusted window size.
