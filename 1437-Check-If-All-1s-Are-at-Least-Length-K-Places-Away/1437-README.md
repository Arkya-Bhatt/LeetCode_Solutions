# 1437. Check If All 1's Are at Least Length K Places Away

**Link:** https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

**Difficulty:** Easy

---

## Problem Statement

Given an binary array `nums` and an integer `k`, return `true` _if all_ `1`_'s are at least_ `k` _places away from each other, otherwise return_ `false`.

---

## Examples

**Example 1:**

![alt text](sample_1_1791.png)
**Input:** nums = [1,0,0,0,1,0,0,1], k = 2 \
**Output:** true \
**Explanation:** Each of the 1s are at least 2 places away from each other.

**Example 2:**

![alt text](sample_2_1791.png)
**Input:** nums = [1,0,0,1,0,1], k = 2 \
**Output:** false \
**Explanation:** The second 1 and third 1 are only one apart from each other.

---

## Constraints

- <code>1 <= nums.length <= 10<sup>5</sup></code>
- `0 <= k <= nums.length`
- `nums[i]` is `0` or `1`

---