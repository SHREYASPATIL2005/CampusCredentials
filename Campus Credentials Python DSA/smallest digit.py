a = 8935
rem = 0
sd = a
while a > 0:
    rem = a % 10  # Gives last digit
    print(rem)
    if rem < sd :
     sd = rem
    a = a // 10 # Removes last digit
    print(a)
print(sd)