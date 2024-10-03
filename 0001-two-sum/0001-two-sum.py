class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        
        for index, value in enumerate(nums):
            diff = target - value
            if diff in myMap:
                return [myMap[diff], index]
            myMap[value] = index
        return