class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        s = 0
        for j in nums:
                if j%2 == 0:
                    s+=j
        # print(s)
        for i in queries:
            if nums[i[1]] % 2 == 0:
                s-=nums[i[1]]
            nums[i[1]]+=i[0]
            if nums[i[1]] % 2 == 0:
                s+=nums[i[1]]
            # else:
            #     s-=nums[i[1]]
            res.append(s)
        return res

        