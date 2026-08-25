class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 1
        if len(nums) == 0:
            return 0

        for num in mySet:
            if num-1 not in mySet:
                count = 1
                while num+1 in mySet:
                    num += 1
                    count += 1
                    
                if count > longest:
                    longest = count
        return longest
