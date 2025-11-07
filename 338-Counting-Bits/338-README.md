# 338. Counting Bits

**Link:** https://leetcode.com/problems/counting-bits/

**Difficulty:** Easy

---

## Problem Statement

Given an integer `n`, return _an array_ `ans` _of length_ `n + 1` _such that for each_ `i` (`0 <= i <= n`), `ans[i]` _is the **number of**_ `1`**'s** _in the binary representation of_ `i`.

## Examples

**Example 1:**

**Input:** n = 2 \
**Output:** [0,1,1] \
**Explanation:** \
0 --> 0 \
1 --> 1 \
2 --> 10

**Example 2:**

**Input:** n = 5 \
**Output:** [0,1,1,2,1,2] \
**Explanation:** \
0 --> 0 \
1 --> 1 \
2 --> 10 \
3 --> 11 \
4 --> 100 \
5 --> 101

---

## Constraints:

- <code>0 <= n <= 10<sup>5</sup></code>

---