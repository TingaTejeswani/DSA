class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        h=len(nums)-1
        while l<=h:
            m=(l+h)//2
            
            if nums[m]==target:
                return True
            if nums[l]==nums[m]==nums[h]:
                l+=1
                h-=1
                continue
            elif nums[l]<=nums[m]:

                if nums[l]<=target<nums[m]:
                    h=m-1
                else:
                    l=m+1
            else:
                if nums[m]<target<=nums[h]:
                    l=m+1
                else:
                    h=m-1
        return False
                

