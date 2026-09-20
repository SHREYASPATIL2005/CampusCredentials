a = 8935
a = 8935
number = abs(a)
rem = 0
sd = number
if number == 0:
    sd = 0
while number > 0:
    rem = number % 10  # Gives last digit
    if rem < sd :
     sd = rem
    number = number // 10 # Removes last digit
print(sd)