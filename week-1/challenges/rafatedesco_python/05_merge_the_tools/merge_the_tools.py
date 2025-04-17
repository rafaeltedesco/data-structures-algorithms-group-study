def merge_the_tools(string, k):
    n = len(string)
    substrings = [] 
    substring = []
    seen = set()
    right = 0
    
    while right < n:
        char = string[right]
        
        if char not in seen:
            seen.add(char)
            substring.append(char)
        
        if (right + 1) % k == 0:
            substrings.append(substring)
            substring = []
            seen = set()  
        
        right += 1  
    
    return [''.join(s) for s in substrings]

if __name__ == '__main__':
    string = "AABCAAADA"
    k = 3
    expected = ["AB", "CA", "AD"]
    result = merge_the_tools(string, k)
    assert result == expected, f"Expected {expected} but got {result}"