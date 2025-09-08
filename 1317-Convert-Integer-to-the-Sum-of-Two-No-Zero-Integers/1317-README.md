# 1317. Convert Integer to the Sum of Two No-Zero Integers

**Link:** https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

**Difficulty:** Easy

---

## Problem Statement

**No-Zero integer** is a positive integer that **does not contain any** `0` in its decimal representation.

Given an integer `n`, return _a list of two integers_ `[a, b]` _where_:

- `a` and `b` are **No-Zero integers**.
- `a + b = n`

The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

---

## Examples

**Example 1:**

**Input:** n = 2 \
**Output:** [1,1] \
**Explanation:** Let a = 1 and b = 1. \
Both a and b are no-zero integers, and a + b = 2 = n.

**Example 2:**

**Input:** n = 11 \
**Output:** [2,9] \
**Explanation:** Let a = 2 and b = 9. \
Both a and b are no-zero integers, and a + b = 11 = n. \
Note that there are other valid answers as [8, 3] that can be accepted.

---

## Constraints

- <code>2 <= n <= 10<sup>4</sup></code>

---