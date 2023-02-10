n = int(input())
list = input().split()

positive = [True if int(x) > 0 else False for x in list]

palindromic = [True if x[::-1] == x else False for x in list]

print(all(positive) and any(palindromic))
