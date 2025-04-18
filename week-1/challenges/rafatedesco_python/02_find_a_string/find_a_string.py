from collections import deque

def count_substring(string, sub_string):
    right = 0
    occurrences = 0
    seen = deque()
    substr_list = deque(sub_string)
    while right < len(string):
        seen.append(string[right])
        if len(seen) == len(sub_string):
            if seen == substr_list:
                occurrences += 1
            seen.popleft()
        right += 1
    
    return occurrences

if __name__ == '__main__':
    count_substring("ABCDCDC", "CDC")
    expected = 2
    result = count_substring("ABCDCDC", "CDC")
    assert result == expected, f"Expected {expected} but got {result}"