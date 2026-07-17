class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2
            
            # if target == nums[mid]:
            #     return target
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid


        pivot = left
        
        def bSearch(l:int ,r: int) -> int:
            while l <= r:
                mid =  (r + l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                
            return -1
        
        res = bSearch(0, pivot - 1)
        if res != -1:
            return res

        return bSearch(pivot, len(nums) - 1)




            