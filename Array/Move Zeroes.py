class Solution(object):
    def moveZeroes(self, nums):
        if (len(nums)==1 and nums[0]==0):
            return
        for i in range (len(nums)):
            if(nums[i]==0):
                nums.remove(nums[i])
                nums.append(0)
        return