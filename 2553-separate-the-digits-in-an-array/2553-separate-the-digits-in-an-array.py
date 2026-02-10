class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        # print(nums)
        res=[]
        for i in nums:
            for c in i:
                res.append(int(c))
        # print(res)
        return res

        