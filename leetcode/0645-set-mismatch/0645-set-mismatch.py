class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0,0]
        check = [i for i in range(1 , len(nums)+1)]
        print(check)
        for i in range(1 , len(nums)):
            if nums[i] == nums[i-1]:
                res[0] = nums[i]
        for i in check:
            if i not in nums:
                res[1] = i
        # if res[1] == 0:

        return res
