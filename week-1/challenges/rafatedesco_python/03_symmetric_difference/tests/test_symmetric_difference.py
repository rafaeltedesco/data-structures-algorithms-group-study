from symmetric_difference import get_symmetric_difference, sorted_set

def test_should_return_symmetric_difference():
    # Given
    a = [10, 20, 30, 40, 50]
    b = [30, 40, 50, 60, 70]
    expected_output = {10, 20, 60, 70}

    # When
    result = get_symmetric_difference(a, b)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_return_empty_set_for_identical_lists():
    # Given
    a = [1, 2, 3]
    b = [1, 2, 3]
    expected_output = set()

    # When
    result = get_symmetric_difference(a, b)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_return_sorted_list():
    # Given
    values = {3, 1, 2}
    expected_output = [1, 2, 3]

    # When
    result = sorted_set(values)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"

def test_should_return_empty_list_for_empty_set():
    # Given
    values = set()
    expected_output = []

    # When
    result = sorted_set(values)

    # Then
    assert result == expected_output, f"Expected {expected_output} but got {result}"