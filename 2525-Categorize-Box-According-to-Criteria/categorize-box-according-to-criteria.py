class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        max_dim = 10**4
        max_vol = 10**9
        vol = length * width * height
        bulky = ((length >= max_dim or width >= max_dim or height >= max_dim) or (vol >= max_vol))
        heavy = (mass >= 100)
        if bulky and heavy:
            return "Both"
        if (not bulky) and (not heavy):
            return "Neither"
        if bulky:
            return "Bulky"
        return "Heavy"