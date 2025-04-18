def swap_case(s):
    return ''.join([letter.lower() if ord(letter) < 97 else letter.upper() for letter in s])



if __name__ == '__main__':
    result = swap_case("Hello World")
    expected = "hELLO wORLD"
    assert result == expected, f"Expected {expected} but got {result}"
