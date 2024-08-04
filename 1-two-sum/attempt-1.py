class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_enumerate = {}
        for index, num in enumerate(nums):
            nums_enumerate[num] = index
        for index, num in enumerate(nums):
            if (complement := target - num) in nums_enumerate and (second_index := nums_enumerate[complement]) != index:
                return [index, second_index]

        return []