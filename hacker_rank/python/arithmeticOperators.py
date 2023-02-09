if __name__ == '__main__':
    a = int(input())
    b = int(input())

    # o que eu pensei originalmente
    # print(a + b)
    # print(a - b)
    # print(a * b)

    # refatorado
    print(f"" + str(a + b) + "\n" + str(a-b) + "\n" + str(a*b))