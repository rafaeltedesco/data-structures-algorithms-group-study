from longest_consecutive_sequence import Solution

def test_should_return_length_of_longest_consecutive_sequence():
    # Given
    nums = [100, 4, 200, 1, 3, 2]
    expected_output = 4

    # When
    result = Solution().longestConsecutive(nums)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_return_zero_for_empty_list():
    # Given
    nums = []
    expected_output = 0

    # When
    result = Solution().longestConsecutive(nums)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_handle_single_element_list():
    # Given
    nums = [10]
    expected_output = 1

    # When
    result = Solution().longestConsecutive(nums)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_handle_list_with_no_consecutive_sequence():
    # Given
    nums = [10, 20, 30]
    expected_output = 1

    # When
    result = Solution().longestConsecutive(nums)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_handle_list_with_duplicates():
    # Given
    nums = [1, 2, 2, 3]
    expected_output = 3

    # When
    result = Solution().longestConsecutive(nums)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"