# 594. Longest Harmonious Subsequence

**Link:** https://leetcode.com/problems/longest-harmonious-subsequence/

**Difficulty:** Easy

---

## Problem Statement

We define a harmonious array as an array where the difference between its maximum value and its minimum value is <b>exactly</b> `1`.

Given an integer array `nums`, return the length of its longest harmonious <b>subsequences</b> among all its possible subsequences.

---

## Examples

**Example 1:**

**Input:** nums = [1,3,2,2,5,2,3,7] \
**Output:** 5 \
**Explanation:** \
The longest harmonious subsequence is <code>[3,2,2,2,3]</code>.

**Example 2:**

**Input:** nums = [1,2,3,4] \
**Output:** 2 \
**Explanation:** \
The longest harmonious subsequences are `[1,2]`, `[2,3]`, and `[3,4]`, all of which have a length of 2.

**Example 3:**

**Input:** nums = [1,1,1,1] \
**Output:** "" \
**Explanation:** \
No harmonic subsequence exists.

---

## Constraints

- <code>1 <= nums.length <= 2 * 10<sup>4</sup></code>
- <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>

---