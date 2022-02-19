class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not t and not s:
            return True
        if not t:
            return False
        stop_here = len(t)
        pointer = 0
        for current_char in s:
            if pointer > stop_here - 1:
                return False
            while current_char != t[pointer] and pointer < stop_here:
                pointer += 1
                if pointer == stop_here:
                    return False
            pointer += 1
        return True