class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount=0
        n=len(nums)
        num_set=set(nums)
        for i in range(n):
            count=1
            while nums[i]+count in num_set:
                    count+=1
        
            if count>maxCount:
                maxCount=count
        return maxCount