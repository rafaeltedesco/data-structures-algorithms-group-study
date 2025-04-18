def swap_case(s):
    new_s = ''
    ascii_c = ''
    output_c = ''
    for c in s:
        ascii_c = ord(c)
        if ascii_c in range(65,91):
            output_c = chr(ascii_c + 32)
        elif ascii_c in range(97,123):
            output_c = chr(ascii_c - 32)
        else:
            output_c = c
        new_s += output_c
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)