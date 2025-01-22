import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = re.search("([a-zA-Z]*)[\s]*?$", s)
        print(x.group(1))
        return 0



Solution().lengthOfLastWord("   fly me   to   the moon  ")