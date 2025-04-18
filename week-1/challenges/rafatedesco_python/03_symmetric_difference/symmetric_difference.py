def get_symmetric_difference(a: list[int], b: list[int]):
    set_a, set_b = set(a), set(b)
    difference = (set_a - set_b) | (set_b - set_a)
    return difference
    
def sorted_set(values: set[int]) -> list[int]:
    if not values:
        return []
    lst = list(values)
    n = len(lst)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                already_sorted = False
        if already_sorted:
            break
    return lst
    
if __name__ == '__main__':
    M = 1
    a = [10, 20, 30, 40, 50]
    N = 1
    b = [30, 40, 50, 60, 70]
    expected = {10, 20, 60, 70}
    result = get_symmetric_difference(a, b)
    assert result == expected, f"Expected {expected} but got {result}"
        
