n = int(input())
creditCards = []
for i in range(n):
    creditCards.append(input())

for cc in creditCards:
    if cc[0] == "4" or cc[0] == "5" or cc[0] == "6":
        if len(cc) == 16:
            if cc.isnumeric():
                if cc.count("0000") >= 1 or cc.count("1111") >= 1 or cc.count("2222") >= 1 or cc.count("3333") >= 1 or cc.count("4444") >= 1 or cc.count("5555") >= 1 or cc.count("6666") >= 1 or cc.count("7777") >= 1 or cc.count("8888") >= 1 or cc.count("9999") >= 1:
                    print("Invalid")
                else:
                    print("Valid")
            else:
                print("Invalid")
        elif len(cc) == 19:
            if cc[4] == "-" and cc[9] == "-" and cc[14] == "-":
                if cc[0:4].isnumeric() and cc[5:9].isnumeric() and cc[10:14].isnumeric() and cc[15:].isnumeric():
                    cc = cc.replace("-", "")
                    if cc.count("0000") >= 1 or cc.count("1111") >= 1 or cc.count("2222") >= 1 or cc.count("3333") >= 1 or cc.count("4444") >= 1 or cc.count("5555") >= 1 or cc.count("6666") >= 1 or cc.count("7777") >= 1 or cc.count("8888") >= 1 or cc.count("9999") >= 1:
                        print("Invalid")
                    else:
                        print("Valid")
                else:
                    print("Invalid")
            else: 
                print("Invalid")
        else: 
            print("Invalid")
    else:
        print("Invalid")