# Day 5: Part 1 

## Problem Description
The task was to simulate a series of operations on a stack of items and determine the final configuration. Each operation specifies how items should be moved between stacks.

## Approach
To solve this problem, I implemented the following steps:
1. **Input Reading**: I read the input data from a file, which contains the initial configuration of stacks and the operations to perform.
2. **Stack Representation**: I used a list of lists to represent the stacks, where each inner list corresponds to a stack of items.
3. **Operation Processing**: I iterated through the list of operations, updating the stacks according to the specified rules for moving items.
4. **Output**: Finally, I printed the final configuration of the stacks after all operations were applied.

This approach effectively simulates the stack operations as described.

## Key Insights
- Using a stack data structure is ideal for this type of problem.
- Clear separation of operations can improve code readability.

## Concepts and Algorithms Used
- **Input Handling**: Reading from files and processing strings.
- **Data Structures**: Lists for representing stacks.
- **Algorithms**: Iteration and simulation of stack operations.