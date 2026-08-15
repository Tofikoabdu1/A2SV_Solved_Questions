class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = [0]
        for i in range(1 , n+1):
            cnt = 0
            while i>0:
                r = i % 2
                if r == 1:
                    cnt +=1
                i=i//2
            ans.append(cnt)
        # print(ans)
        return ans
        