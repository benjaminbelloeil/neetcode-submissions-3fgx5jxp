class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in char:
                char[i] += 1
            else:
                char[i] = 1
        
        for j in t:
            if j not in char:
                return False

            char[j] -= 1

            if char[j] < 0:
                return False

        if char:
            return True