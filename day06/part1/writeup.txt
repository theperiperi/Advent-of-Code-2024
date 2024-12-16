# Day 6: Part 1 

## Problem Description
The challenge was to analyze a sequence of characters and determine the first position where a specific condition is met. The condition typically involves finding a unique sequence of characters.

## Approach
To solve this problem, I implemented the following steps:
1. **Input Reading**: I read the input data from a file, which contains a long string of characters.
2. **Sliding Window Technique**: I used a sliding window approach to examine substrings of the input string. This technique allows for efficient checking of conditions over a sequence.
3. **Condition Checking**: For each position in the string, I checked if the substring within the window met the specified condition (e.g., all characters being unique).
4. **Output**: Finally, I printed the position where the condition was first met.

This approach is efficient and leverages the sliding window technique for optimal performance.

## Key Insights
- Using a sliding window approach can optimize the search for conditions in sequences.
- Efficiently managing state within the window is key to performance.

## Concepts and Algorithms Used
- **Input Handling**: Reading from files and processing strings.
- **Data Structures**: Strings for character sequences.
- **Algorithms**: Sliding window technique for condition checking.
