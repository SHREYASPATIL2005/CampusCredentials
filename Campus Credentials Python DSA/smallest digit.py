a = 8935
# Original version kept for comparison; it returned the negative input unchanged.
# rem = 0
# sd = a
# while a > 0:
#     rem = a % 10
#     print(rem)
#     if rem < sd:
#         sd = rem
#     a = a // 10
#     print(a)

# Use the absolute value so negative numbers are processed by digit value.
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