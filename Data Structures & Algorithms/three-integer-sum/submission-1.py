class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-1,0,1,2,-1,-4]
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    # insert numbers that equal to 0 to an array
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        tmp.sort()
                        res.add(tuple(tmp))

        return [list(t) for t in res]   

    
# return a list of arrays that contains 3 numbers each (without duplicates)
# in which the sum of those 3 numbers equals 0
# List of array can be in any order
# Array of number can be in any order