a = 8935
rem = 0
ld = 0
while a > 0:
    rem = a % 10  # Gives last digit
    print(rem)
    if rem > ld :
     ld = rem
    a = a // 10 # Removes last digit
    print(a)
print(ld)