class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict() # element : index
        # Create an empty hash table, and iterate the input list, to insert them to the hash Table.
        # When inserting, check if the subtraction of the target and the current element is already present in the hash Table.
        # This ensures, the list is traversed only once, at the cost of O(n) space complexity.
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashTable:
                return [hashTable[diff], i]
            hashTable[nums[i]] = i