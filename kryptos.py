import random
import string

counter = 0
f = open("k4.txt",'a')

# def generator():
#     # if 22nd is E
#     global counter
#     plain = ''
#     for i in range(97):
#         ch = random.choice(string.ascii_uppercase)
#         if i == 21 and ch != 'E':
#             break
#         else:
#             plain = plain + ch
#     print(counter)
#     if plain[21:35] == "EASTNORTHEAST" and plain[63-70] == "BERLIN" and plain[69:75] == "CLOCK":
#         f.write(f"{plain}\n")
#         print(plain)
#         counter +=1

freq = [8,2,3,4,13,2,2,6,7,1,1,4,2,7,8,2,1,6,6,9,3,1,2,1,2,1]

def generator2():

    part1 = random.choices(string.ascii_uppercase, weights=freq, k=21)
    part2 = random.choices(string.ascii_uppercase, weights=freq, k=29)
    part3 = random.choices(string.ascii_uppercase, weights=freq, k=5)

    full = part1+"EASTNORTHEAST"+part2+"BERLINCLOCK"+part3
    f.write(full)
    counter += 1
        
print("Starting to generate...\n")
print("Generated strings in file k4.txt")

while counter <= 10^6:
    generator2()

print("Done.")

# j = open("k4.txt", 'r')

# def cleaner():
#     while True:
#         line = j.readline()
#         if not line:
#             break
#         if len(line) > 21:
#             f.write(f"{line}\n")
#         else:
#             continue

# cleaner()
# print("done.")