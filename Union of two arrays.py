class Solution:    
    def findUnion(self, a, b):
        # code here
        s1 = set(a)
        s2 = set(b)
        s3 = s1.union(s2)
        return list(s3)
