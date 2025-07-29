class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a=s+s
        if len(s)!=len(goal):
            return False
        if goal in a:
            return True
        else:
            return False