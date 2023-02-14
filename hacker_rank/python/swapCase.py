def swap_case(s):
    swapedString = ""
    for l in s:
        if l.islower():
            swapedString += l.upper()
        else:
            swapedString += l.lower()
    return swapedString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)