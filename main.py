import random

table = "OABCDESGHN"
table1 = "0123456789"
encode = []

nn = input("Tryout:")
if nn.capitalize() == "Y":
    while True:
        encode = list(input())
        encode = [x.capitalize() for x in encode]
        encode1 = ""
        for x in range(len(encode)):
            encode1 += str(table.find(encode[x]))
        if encode1.find("-1") == -1:
            print(encode1)
        else: print("Incorrect encoding")


n = input("Zeros:")
c1 = input("Reveal y/n:").capitalize()
c2 = input("Reverse y/n:").capitalize()

if n.isdigit(): zeros = int(n) 
else: zeros = 6
if c1 not in ("Y","N"): c1 = ""
if c2 not in ("Y","N"): c2 = ""
if c1 != "N": reveal = True
else: reveal = False
if c2 != "Y": reverse = False
else: reverse = True

while True:    
    last = random.randint(10**zeros, (10**(zeros+1))-1)
    
    # Encode
    encode = list(str(last))
    encode1 = ""
    for x in range(len(encode)):
        encode1 += table[int(encode[x])]

    
    if reveal and reverse:
        print(encode1)
        print(last)
        input()
        #os.system("cls")
    elif reverse:
        print("*", encode1)
        a = input("G ")
        #os.system("cls")
        print("#", last)
        input()
        #os.system("cls")
    elif reveal:
        print(last)
        print(encode1)
        input()
        #os.system("cls")
    else:
        print("#", last)
        a = input("G ")
        #os.system("cls")
        #print(last)
        print("*", encode1)
        input()
        #os.system("cls")
