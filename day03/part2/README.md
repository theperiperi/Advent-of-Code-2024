# Day 3: Part 2 - [Problem Name]

## Problem Description
In this part, the task was to find the common character across multiple strings and calculate a score based on its position in the alphabet. The goal was to identify the character that appears in all strings and determine its score.

## Approach
To tackle this problem, I followed these steps:
1. **Reuse Previous Logic**: I reused the character counting logic from Part 1 to maintain consistency.
2. **Identify Common Character**: I created a set for each string to facilitate the intersection operation, which allows me to find characters that appear in all strings.
3. **Calculate Score**: Once the common character was identified, I calculated its score based on its position in the alphabet (e.g., 'a' = 1, 'b' = 2, etc.).
4. **Output**: Finally, I printed the score of the common character.

This approach efficiently identifies the common character and calculates its score.

## Key Insights
- Reusing code can save time and reduce errors.
- Scoring based on character position can be efficiently calculated using ASCII values.

## Concepts and Algorithms Used
- **Input Handling**: Reading from files and processing strings.
- **Data Structures**: Sets for identifying common characters.
- **Algorithms**: Intersection of sets and scoring based on character position.