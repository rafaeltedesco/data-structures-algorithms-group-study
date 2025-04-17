class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in set_nums:

            if num -1 not in set_nums:
                current=num
                streak = 1

                while current+1 in set_nums:
                    streak += 1
                    current += 1

                longest = max(longest, streak)
        return longest

if __name__ == '__main__':
    # Example usage
    nums = [100, 4, 200, 1, 3, 2]
    expected = 4
    result = Solution().longestConsecutive(nums)
    assert result == expected, f"Expected {expected} but got {result}"