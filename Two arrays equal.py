from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        d = Counter(a)
        e = Counter(b)
        if d==e:
            return True
        else:
            return False
