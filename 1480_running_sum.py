class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        running_sum=[]
        runningTotal=0

        for num in nums:
            runningTotal+=num
            running_sum.append(runningTotal)

        return running_sum

