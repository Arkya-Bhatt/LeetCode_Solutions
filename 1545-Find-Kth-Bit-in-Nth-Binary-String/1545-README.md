# 1545. Find Kth Bit in Nth Binary String

**Link:** https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

**Difficulty:** Medium

---

## Problem Statement

Given two positive integers `n` and `k`, the binary string <code>S<sub>n</sub></code> is formed as follows:

- <code>S<sub>1</sub> = "0"</code>
- <code>S<sub>i</sub> = S<sub>i - 1</sub> + "1" + reverse(invert(S<sub>i - 1</sub>))</code> for `i > 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string `x`, and `invert(x)` inverts all the bits in `x` (`0` changes to `1` and `1` changes to `0`).

For example, the first four strings in the above sequence are:

- <code>S<sub>1</sub> = "0"</code>
- <code>S<sub>2</sub> = "011"</code>
- <code>S<sub>3</sub> = "0111001"</code>
- <code>S<sub>4</sub> = "011100110110001"</code>

Return _the_ <code>k<sup>th</sup></code> _bit in_ <code>S<sub>n</sub></code>. It is guaranteed that `k` is valid for the given `n`.

---

## Examples

**Example 1:**

**Input:** n = 3, k = 1 \
**Output:** "0" \
**Explanation:** S<sub>3</sub> is "<u>**0**</u>111001".
The 1<sup>st</sup> bit is "0".

**Example 2:**

**Input:** n = 4, k = 11 \
**Output:** "1" \
**Explanation:** S<sub>4</sub> is "0111001101<u>**1**</u>0001".
The 11<sup>th</sup> bit is "1".

---

## Constraints

- `1 <= n <= 20`
- <code>1 <= k <= 2<sup>n</sup> - 1</code>

---