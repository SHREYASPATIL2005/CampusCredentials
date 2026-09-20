a = 8935
# Original version kept for comparison; it did not handle negative input.
# rem = 0
# ld = 0
# while a > 0:
#     rem = a % 10
#     print(rem)
#     if rem > ld:
#         ld = rem
#     a = a // 10
#     print(a)

# Use the absolute value so negative numbers are processed by digit value.
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