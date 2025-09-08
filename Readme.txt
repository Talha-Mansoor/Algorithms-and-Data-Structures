Project Index — Mixed Java and Python Files

Folders
-------
File Read and Edit Python   - Python utilities for file I/O
Java OOP                    - Java programs demonstrating OOP concepts and Data Structures
Node Chain                  - Linked node/chain data structure examples
Recursion_Binary_Tree       - Recursive binary tree implementations
Simple Sudoku               - Sudoku solver or generator (logic-based)
Algorithms                  -Recursion, Divide-and-Conquer, Backtracking, Recurrence Relations, Dynamic Programming, Tree Traversal, Geometry Partitioning 


Standalone Python Files
-----------------------
CardShuffle.py              - card shuffle simulation
Fibonacci.py                - Fibonacci sequence generator
Linked_List.py              - linked list implementation in Python
Simple Student List Python.py - basic student list management
(Simple Student List)

Standalone Java Files
---------------------
Matrix_Rotation.java        - 3x3 matrix rotation puzzle
Simple_Interpreter.java     - small command interpreter (register + heap)
PetStore.Jar                -An Executable file with gui that can run from terminal using 'java -jar PetStore.jar'


<-------------------->


Algorithms

Grid.java   - Implements recursion and divide-and-conquer logic over a grid structure.
Image.java  - Solves a linear recurrence relation problem, typical of backtracking/dynamic programming.
Minion-1.java - Reverse recurrence puzzle (“spend money” problem), demonstrating recurrence and closed-form solutions.
T.java      - Recursive subdivision of a triangle using a ternary tree, related to divide-and-conquer geometry.
T2.java     - Variation of triangle partitioning with centroid-based recursion, showing backtracking and recursive structure traversal.


<-------------------->


Java OOP
CMPT 280 Assignments — Java File Index

Assignment 1 — Lists & Iterators
--------------------------------
LinkedList280.java       - singly linked list
BilinkedList280.java     - doubly linked list
LinkedIterator280.java   - forward iterator
BilinkedIterator280.java - bidirectional iterator
LinkedNode280.java       - singly node
BilinkedNode280.java     - doubly node
CargoSimulator.java      - demo data/driver
Ship.java                - ship cargo model
Sack.java                - grain sack model
Main.java                - CLI entrypoint
*Solution.java           - instructor/demo solution

Assignment 3 — Trees
---------------------
ArrayedBinaryTreeWithCursors280.java - array tree + cursor
BasicMAryTree280.java                 - generic m-ary tree
Skill.java                            - skill node record
SkillTree.java                        - game skill tree

Assignment 5 — Heaps, Restriction, Hashing
-------------------------------------------
ArrayedBinaryTreeIterator280.java - array-tree iterator
IterableArrayedHeap280.java        - heap with iterator
PriorityQueue280.java              - heap-backed priority queue
QuestLogEntry.java                 - quest record (keyed)
QuestLog.java                      - chained hash table (quests)

Assignment 6 — 2-3 / B+ Tree (order 3)
---------------------------------------
TwoThreeTree280.java           - 2-3 tree (keyed)
LinkedLeafTwoThreeNode280.java - leaf links (prev/next)
IterableTwoThreeTree280.java   - B+-style iterator tree
main() tests                   - regression/iterator tests

Assignment 7 — k-D Tree (and Graph background)
-----------------------------------------------
KDNode280.java   - k-d tree node
KDTree280.java   - k-d tree + range search
Partition/Select - selection and partition helpers
Topo*/Graph*     - topological sort utilities (if present)

Notes
-----
- Each assignment uses a matching lib280 version (lib280-asn1, lib280-asn5, etc.).
- ADTs follow iterator/cursor interfaces from lib280.
- Keyed data structures use hash tables or trees with ordered iteration.
