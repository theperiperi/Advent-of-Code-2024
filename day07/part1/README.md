# Day 7: Part 1 - [Problem Name]

## Problem Description
The task was to analyze a file system structure and determine the total size of directories that meet specific criteria. The input consists of a representation of the file system, including files and directories.

## Approach
To solve this problem, I implemented the following steps:
1. **Input Reading**: I read the input data from a file, which contains the structure of the file system.
2. **Tree Representation**: I built a tree representation of the file system, where each node represents a directory or file.
3. **Size Calculation**: I traversed the tree to calculate the sizes of directories, summing the sizes of their contents.
4. **Output**: Finally, I printed the total size of the directories that meet the specified criteria.

This approach effectively models the file system and calculates sizes based on the structure.

## Key Insights
- Using a tree structure is effective for representing hierarchical data like file systems.
- Recursive traversal can simplify the logic for calculating sizes.

## Concepts and Algorithms Used
- **Input Handling**: Reading from files and processing strings.
- **Data Structures**: Trees for representing file systems.
- **Algorithms**: Recursive traversal for size calculation.