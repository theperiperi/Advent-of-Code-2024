# Day 2: Part 1 - [Problem Name]

## Problem Description
The task was to determine the total score based on a series of game rounds, where each round's outcome affects the total score. The scoring system is defined by specific rules that map the outcomes to numerical values.

## Approach
To solve this problem, I implemented the following steps:
1. **Input Reading**: I read the input data from a file, which contains the outcomes of each game round.
2. **Scoring Mapping**: I created a dictionary to map each possible outcome to its corresponding score. This allows for quick lookups when processing each round.
3. **Iterate Through Rounds**: I iterated through each round's outcome, using the dictionary to retrieve the score for each outcome and accumulating the total score.
4. **Output**: Finally, I printed the total score after processing all rounds.

This approach is efficient and leverages Python's dictionary for fast lookups.

## Key Insights
- Using dictionaries for mapping outcomes to scores simplifies the logic and makes the code more readable.
- Iterating through the input data efficiently is key to maintaining performance.

## Concepts and Algorithms Used
- **Input Handling**: Reading from files and processing strings.
- **Data Structures**: Dictionaries for mapping outcomes to scores.
- **Algorithms**: Iteration and accumulation of scores.