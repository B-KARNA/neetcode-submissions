class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set(nums)
        ''' for i in nums:
            if i in seen:
                return True
            seen.add(nums)
        return False '''
        a=len(nums)
        b=len(seen)
        if a!=b:
            return True
        else:
            return False