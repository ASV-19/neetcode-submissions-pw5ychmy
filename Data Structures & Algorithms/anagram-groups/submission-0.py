class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # for the 26 lowercase alphabets
            for c in s:
                count[ord(c) - ord('a')] += 1 # to ensure 'a' is given 0th index, while 'z' is given 25th index in the count list

            result[tuple(count)].append(s)

        return list(result.values())