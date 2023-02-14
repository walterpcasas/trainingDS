if __name__ == '__main__':
    s = input()
    print(any([True if l.isalnum() else False for l in s]))
    print(any([True if l.isalpha() else False for l in s]))
    print(any([True if l.isdigit() else False for l in s]))
    print(any([True if l.islower() else False for l in s]))
    print(any([True if l.isupper() else False for l in s]))