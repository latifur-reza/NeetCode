class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myMap = set()

        for val in nums:
            if val in myMap:
                return True
            myMap.add(val)
        return False
        