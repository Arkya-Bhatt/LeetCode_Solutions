# 76. Minimum Window Substring

**Link:** https://leetcode.com/problems/minimum-window-substring/

**Difficulty:** Hard

---

## Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return _the **minimum window substring** of s such that every character in `t` (**including duplicates**) is included in the window_. If there is no such substring, return _the empty string_ `""`.

The testcases will be generated such that the answer is **unique**.

---

## Examples

**Example 1:**

**Input:** s = "ADOBECODEBANC", t = "ABC" \
**Output:** "BANC" \
**Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

**Example 2:**

**Input:** s = "a", t = "a" \
**Output:** "a" \
**Explanation:** The entire string s is the minimum window.

**Example 3:**

**Input:** s = "a", t = "aa" \
**Output:** "" \
**Explanation:** Both 'a's from t must be included in the window. \
Since the largest window of s only has one 'a', return empty string.

---

## Constraints

- `m == s.length`
- `n == t.length`
- <code>1 <= m, n <= 10<sup>5</sup></code>
- `s` and `t` consist of uppercase and lowercase English letters.

---