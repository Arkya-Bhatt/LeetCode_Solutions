# 74. Search a 2D Matrix

**Link:** https://leetcode.com/problems/search-a-2d-matrix/

**Difficulty:** Medium

---

## Problem Statement

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` _if_ `target` _is in_ `matrix` _or_ `false` _otherwise_.

You must write a solution in **O(log(m * n))** time complexity.

---

## Examples

**Example 1:**

![alt text](mat.jpg)
**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 \
**Output:** true

**Example 2:**

![alt text](mat2.jpg)
**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 \
**Output:** false

---

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- <code>-10<sup>4</sup> <= matrix[i][j], target <= 10<sup>4</sup> </code>

---