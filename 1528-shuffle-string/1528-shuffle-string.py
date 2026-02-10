class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        coll = []
        for i in range(len(s)):
            coll.append([indices[i],s[i]])
        coll.sort()
        res = []
        for i in coll:
            res.append(i[1])
        return "".join(res)
        