a = 8935
a = 8935
number = abs(a)
rem = 0
ld = 0
if number == 0:
    ld = 0
while number > 0:
    rem = number % 10  # Gives last digit
    if rem > ld :
     ld = rem
    number = number // 10 # Removes last digit
print(ld)