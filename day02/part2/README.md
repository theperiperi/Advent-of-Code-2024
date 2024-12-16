# Day 2: Part 2

## Problem Description
In this part, the goal was to adjust the scoring based on additional rules that modified how scores were calculated from the game rounds. The new rules introduced complexity in determining the final score.

## Approach
To tackle this problem, I followed these steps:
1. **Reuse Previous Logic**: I reused the scoring logic from Part 1 to maintain consistency and reduce redundancy.
2. **Adjust Scoring Rules**: I modified the scoring mapping to accommodate the new rules. This involved updating the dictionary to reflect the changes in how scores are calculated.
3. **Iterate Through Rounds**: I iterated through each round's outcome again, applying the updated scoring rules to calculate the total score.
4. **Output**: Finally, I printed the adjusted total score after processing all rounds.

This approach maintains clarity by building on the existing logic while incorporating the new rules.

## Key Insights
- Extending existing logic can be done efficiently by building on previous implementations.
- Clear documentation of rules is essential for maintaining code clarity.

## Concepts and Algorithms Used
- **Input Handling**: Reading from files and processing strings.
- **Data Structures**: Dictionaries for mapping outcomes to scores.
- **Algorithms**: Iteration and accumulation of scores with adjusted rules.