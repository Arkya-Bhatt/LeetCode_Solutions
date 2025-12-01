from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck, reverse=True)
        q = deque()
        for card in sorted_deck:
            if q:
                q.appendleft(q.pop())
            q.appendleft(card)
        return list(q)
        