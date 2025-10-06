# 238. Product of Array Except Self

**Link:** https://leetcode.com/problems/product-of-array-except-self/

**Difficulty:** Medium

---

## Problem Statement

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

---

## Examples

**Example 1:**

**Input:** nums = [1,2,3,4] \
**Output:** [24,12,8,6]

**Example 2:**

**Input:** nums = [-1,1,0,-3,3] \
**Output:** [0,0,9,0,0]

---

## Constraints

- <code>2 <= nums.length <= 10<sup>5</sup></code>
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

---