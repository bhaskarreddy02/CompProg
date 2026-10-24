class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        if (event1[0]<=event2[0] and event2[0]<=event1[1]) or (event2[0]<=event1[0] and event1[0]<=event2[1]):
            return True
        return False    