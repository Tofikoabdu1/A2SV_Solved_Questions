#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        s = Counter(a)
        for i in b:
            if i in s:
                if s[i]==0:
                    return False
                else:
                    s[i]-=1
            else:
                return False
        return True
            
    
    
    
    
