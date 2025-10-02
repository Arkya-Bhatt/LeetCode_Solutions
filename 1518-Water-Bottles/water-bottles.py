class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty_bottles = numBottles
        
        while empty_bottles >= numExchange:
            
            new_full_bottles = empty_bottles // numExchange
            
            total_drunk += new_full_bottles
            
            bottles_leftover = empty_bottles % numExchange
            
            empty_bottles = bottles_leftover + new_full_bottles
            
        return total_drunk
        