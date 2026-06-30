class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ''' n=len(numbers)
        for i in range(0,n):
            for j in range(i+1,n):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
 '''
        l,r=0,len(numbers)-1
        while l<r:
            curr_sum=numbers[l]+numbers[r]
            if curr_sum==target:
                return [l+1,r+1]
            elif curr_sum>target:
                r-=1
            else:
                l+=1
