class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        k = len(nums)

        while l < k:
            if nums[l] == val:
                nums[l] = nums[k-1]
                k -= 1
            elif nums[l] != val:
                l += 1
        return k