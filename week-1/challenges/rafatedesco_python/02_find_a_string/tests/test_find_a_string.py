from find_a_string import count_substring

def test_should_count_single_occurrence():
    # Given
    string = "hello"
    sub_string = "lo"
    expected_output = 1

    # When
    result = count_substring(string, sub_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_count_multiple_occurrences():
    # Given
    string = "ABCDCDC"
    sub_string = "CDC"
    expected_output = 2

    # When
    result = count_substring(string, sub_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_return_zero_for_no_occurrence():
    # Given
    string = "hello"
    sub_string = "world"
    expected_output = 0

    # When
    result = count_substring(string, sub_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_count_overlapping_occurrences():
    # Given
    string = "aaaa"
    sub_string = "aa"
    expected_output = 3

    # When
    result = count_substring(string, sub_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_return_zero_for_empty_substring():
    # Given
    string = "hello"
    sub_string = ""
    expected_output = 0

    # When
    result = count_substring(string, sub_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_return_zero_for_empty_string():
    # Given
    string = ""
    sub_string = "hello"
    expected_output = 0

    # When
    result = count_substring(string, sub_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"