# Day 13: Part 1 

## Problem Description
The task was to analyze a series of pairs and determine their order based on specific comparison rules. Each pair consists of two elements that need to be compared according to the defined criteria. The goal is to establish which element in each pair is considered "greater" based on the rules provided.

## Approach
To solve this problem, I implemented the following steps:
1. **Input Reading**: I read the input data from a file, which contains multiple pairs of elements.
2. **Parsing Pairs**: I parsed the input to extract each pair and stored them in a list for easy access.
3. **Comparison Logic**: I defined a comparison function that implements the specific rules for determining the order of the elements in each pair. This function is called for each pair to evaluate their order.
4. **Count Ordered Pairs**: I maintained a count of how many pairs are in the correct order according to the defined rules.
5. **Output**: Finally, I printed the count of correctly ordered pairs.

This approach effectively evaluates the order of pairs based on the specified rules.

## Key Insights
- Using a custom comparison function allows for flexibility in defining the ordering criteria.
- Efficiently parsing and processing pairs is key to maintaining performance.

## Concepts and Algorithms Used
- **Input Handling**: Reading from files and processing strings.
- **Data Structures**: Lists for storing pairs of elements.
- **Algorithms**: Custom comparison logic and iteration for counting ordered pairs.