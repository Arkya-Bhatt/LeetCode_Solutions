# 89. Gray Code

**Link:** https://leetcode.com/problems/gray-code/

**Difficulty:** Medium

---

## Problem Statement

An <b>n-bit gray code sequence</b> is a sequence of <code>2<sup>n</sup></code> integers where:

- Every integer is in the <b>inclusive</b> range `[0, 2n - 1]`,
- The first integer is `0`,
- An integer appears <b>no more than once</b> in the sequence,
- The binary representation of every pair of <b>adjacent</b> integers differs by <b>exactly one bit</b>, and
- The binary representation of the <b>first</b> and <b>last</b> integers differs by <b>exactly one bit</b>.

## Examples

**Example 1:**

**Input:** n = 2 \
**Output:** [0,1,3,2] \
**Explanation:** \
The binary representation of [0,1,3,2] is [00,01,11,10]. \
--- 0<u>0</u> and 0<u>1</u> differ by one bit \
--- <u>0</u>1 and <u>1</u>1 differ by one bit \
--- 1<u>1</u> and 1<u>0</u> differ by one bit \
--- <u>1</u>0 and <u>0</u>0 differ by one bit \
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01]. \
--- <u>0</u>0 and <u>1</u>0 differ by one bit \
--- 1<u>0</u> and 1<u>1</u> differ by one bit \
--- <u>1</u>1 and <u>0</u>1 differ by one bit \
--- 0<u>1</u> and 0<u>0</u> differ by one bit

**Example 2:**

**Input:** n = 1 \
**Output:** [0,1]

---

## Constraints:

- <code>1 <= n <= 16</code>

---