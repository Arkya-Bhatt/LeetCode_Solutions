class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        rem   = n % 7
        firstWeekSum = 28
        if weeks > 0:
            lastWeekSum = firstWeekSum + 7 * (weeks - 1)
            sumFull = (firstWeekSum + lastWeekSum) * weeks // 2
        else:
            sumFull = 0
        sumRem = ( (weeks + 1) + (weeks + rem) ) * rem // 2
        return sumFull + sumRem
        