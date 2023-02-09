if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = list(arr)
    
    list.sort()
    
    maximum = list[0]
    runner_up = list[0]
    for i in list:   
        if i > maximum:
            runner_up = maximum
            maximum = i
    
    print(runner_up)