from swap_case import swap_case

def test_should_swap_case_given_input_string_with_mixed_case():
    # Given
    input_string = "Hello World"
    expected_output = "hELLO wORLD"

    # When
    result = swap_case(input_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_swap_case_given_empty_string():
    # Given
    input_string = ""
    expected_output = ""

    # When
    result = swap_case(input_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_swap_case_given_string_with_numbers():
    # Given
    input_string = "Hello123"
    expected_output = "hELLO123"

    # When
    result = swap_case(input_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_swap_case_given_string_with_special_characters():
    # Given
    input_string = "Hello@World!"
    expected_output = "hELLO@wORLD!"

    # When
    result = swap_case(input_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_swap_case_given_string_with_only_lowercase():
    # Given
    input_string = "hello world"
    expected_output = "HELLO WORLD"

    # When
    result = swap_case(input_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_swap_case_given_string_with_only_uppercase():
    # Given
    input_string = "HELLO WORLD"
    expected_output = "hello world"

    # When
    result = swap_case(input_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_swap_case_given_string_with_multiple_with_spaces():
    # Given
    input_string = "  Hello   World  "
    expected_output = "  hELLO   wORLD  "

    # When
    result = swap_case(input_string)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"
