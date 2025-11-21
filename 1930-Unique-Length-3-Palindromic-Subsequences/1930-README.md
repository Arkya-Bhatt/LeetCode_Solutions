# 1930. Unique Length-3 Palindromic Subsequences

**Link:** https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

**Difficulty:** Medium

---

## Problem Statement

Given a string `s`, return _the number of **unique palindromes of length three** that are a **subsequence** of_ `s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once**.

A **palindrome** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of <code>"<u>a</u>b<u>c</u>d<u>e</u>"</code>.


---

## Examples

**Example 1:**

**Input:** s = "aabca" \
**Output:** 3 \
**Explanation:** The 3 palindromic subsequences of length 3 are: \
-- "aba" (subsequence of "<u>a</u>a<u>b</u>c<u>a</u>") \
-- "aaa" (subsequence of "<u>a</u><u>a</u>bc<u>a</u>") \
-- "aca" (subsequence of "<u>a</u>ab<u>c</u><u>a</u>")

**Example 2:**

**Input:** s = "adc" \
**Output:** 0 \
**Explanation:** There are no palindromic subsequences of length 3 in "adc".

**Example 3:**

**Input:** s = "bbcbaba" \
**Output:** 4 \
**Explanation:** The 4 palindromic subsequences of length 3 are: \
-- "bbb" (subsequence of "<u>b</u><u>b</u>c<u>b</u>aba") \
-- "bcb" (subsequence of "<u>b</u>b<u>c</u><u>b</u>aba") \
-- "bab" (subsequence of "<u>b</u>bcb<u>a</u><u>b</u>a") \
-- "aba" (subsequence of "bbcb<u>a</u><u>b</u><u>a</u>")

---

## Constraints

- <code>3 <= s.length <= 10<sup>5</sup></code>
- `s` consists of only lowercase English letters.

---