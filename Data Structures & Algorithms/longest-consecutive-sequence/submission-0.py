class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        l1 = sorted(nums)
        longest_streak = 1
        current_streak = 1
        for i in range(1, len(l1)):
            if l1[i] == l1[i-1]:
                continue
            if l1[i] == l1[i-1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
        return max(longest_streak, current_streak)

