import random
import string

counter = 0
f = open("k4.txt",'a')

def generator():
    # if 22nd is E
    plain = ''
    for i in range(97):
        ch = random.choice(string.ascii_uppercase)
        if i == 21 and ch != 'E':
            break
        else:
            plain = plain + ch
    f.write(f"{plain}\n")
    print(plain)
    global counter
    counter +=1

while counter <= 1000 + 26^22:
    generator()

j = open("k4.txt", 'r')

def cleaner():
    while True:
        line = j.readline()
        if not line:
            break
        if len(line) > 21:
            f.write(f"{line}\n")
        else:
            continue

cleaner()
print("done.")