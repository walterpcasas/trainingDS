if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    permutations = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

    # o que eu originalmente pensei
    # list = []    
    # for i in permutations:
    #     if sum(i) != n:
    #         list.append(i)

    list = [i for i in permutations if sum(i) != n]

    # print(permutations)
    print(list)