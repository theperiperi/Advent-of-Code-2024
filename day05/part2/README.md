# Day 5: Part 2 

## Problem Description
In this part, the goal was to modify the stack operations to accommodate additional rules. The new rules changed how items could be moved between stacks, affecting the final configuration.

## Approach
To tackle this problem, I followed these steps:
1. **Reuse Previous Logic**: I reused the stack representation and input reading logic from Part 1 to maintain consistency.
2. **Adjust Operation Rules**: I modified the logic for moving items between stacks to reflect the new rules. This involved changing how many items could be moved at once and the order in which they were moved.
3. **Operation Processing**: I iterated through the list of operations again, applying the updated rules to calculate the final configuration of the stacks.
4. **Output**: Finally, I printed the adjusted final configuration of the stacks.

This approach maintains clarity by building on the existing logic while incorporating the new rules.

## Key Insights
- Extending existing logic can be done efficiently by building on previous implementations.
- Clear documentation of new rules is essential for maintaining code clarity.

## Concepts and Algorithms Used
- **Input Handling**: Reading from files and processing strings.
- **Data Structures**: Lists for representing stacks.
- **Algorithms**: Iteration and simulation of stack operations with adjusted rules.