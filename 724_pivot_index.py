class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left_sum=0
        right_sum=sum(nums)

        for i in range(len(nums)):

            if i>0:
                left_sum+=nums[i-1]
            
            if i<len(nums):
                right_sum-=nums[i]

            if (left_sum==right_sum):
                return i
        
        return -1
            