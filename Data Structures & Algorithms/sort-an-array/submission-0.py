class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            swapped = False

            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if swapped == False:
                break
        return nums



# Bubble sort
# Sort the array based on the next element
# Has to be in a range of elements
# remeber last element is already sorted

