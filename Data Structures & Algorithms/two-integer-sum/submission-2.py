class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()
        # Create an empty hash table, and iterate the input list, to insert them to the hash Table.
        # When inserting, check if the subtraction of the target and the current element is already present in the hash Table.
        # This ensures, the list is traversed only once, at the cost of O(n) space complexity.
        if len(nums) == 2:
            return [0,1]
        for i in range(0, len(nums), 1):
            if target - nums[i] not in hashTable.keys():
                hashTable[nums[i]] = i
            else:
                return [hashTable[target-nums[i]], i]