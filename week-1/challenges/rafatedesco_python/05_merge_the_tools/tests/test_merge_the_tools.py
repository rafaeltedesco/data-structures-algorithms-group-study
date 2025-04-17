from merge_the_tools import merge_the_tools

def test_should_split_and_remove_duplicates():
    # Given
    string = "AABCAAADA"
    k = 3
    expected_output = ["AB", "CA", "AD"]

    # When
    result = merge_the_tools(string, k)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_handle_string_with_all_duplicates():
    # Given
    string = "AAAAAA"
    k = 2
    expected_output = ["A", "A", "A"]

    # When
    result = merge_the_tools(string, k)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_handle_empty_string():
    # Given
    string = ""
    k = 3
    expected_output = []

    # When
    result = merge_the_tools(string, k)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"
