string = input()

lowercase = [l for l in string if l.islower()]
uppercase = [l for l in string if l.isupper()]
odds = [l for l in string if l.isdigit() and int(l) % 2 != 0]
evens = [l for l in string if l.isdigit() and int(l) % 2 == 0]

lowercase.sort()
uppercase.sort()
odds.sort()
evens.sort()

sortedString = ''.join(lowercase) + ''.join(uppercase) + ''.join(odds) + ''.join(evens)
print(sortedString)