class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        # res = [-1] * max(nums)
        if n<2:
            return 0
        #cyclic sorting 
        # for i in range(n):
        #     while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        temp = 0
        print(nums)
        for i in range(1 , len(nums)):
            d = nums[i]-nums[i-1]
            temp = max(temp , d)
        return temp
        
        