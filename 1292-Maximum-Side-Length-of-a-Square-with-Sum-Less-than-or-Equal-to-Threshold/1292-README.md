# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

**Link:** https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

**Difficulty:** Medium

---

## Problem Statement

Given a `m x n` matrix `mat` and an integer `threshold`, return _the maximum side-length of a square with a sum less than or equal to_ `threshold` _or return_ `0` _if there is no such square_.

---

## Examples

**Example 1:**

![alt text](image.png) \
**Input:** mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4 \
**Output:** 2 \
**Explanation:** The maximum side length of square with sum less than 4 is 2 as shown.

**Example 2:**

**Input:** mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1 \
**Output:** 0

---

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 300`
- <code>0 <= mat[i][j] <= 10<sup>4</sup></code>
- <code>0 <= threshold <= 10<sup>5</sup></code>

---