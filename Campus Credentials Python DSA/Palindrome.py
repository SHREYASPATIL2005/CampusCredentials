
a = 121
# Original version kept as a commented learning example:
# temp = a
# rev = 0
# digit_sum = 0
# while a > 0:
#     rem = a % 10
#     digit_sum += rem
#     print(rem)
#     rev = rev * 10 + rem
#     a = a // 10
#     print(a)
#     print(rev)
# if rev == temp:
#     print("Pallindrome")

# The corrected version also handles negative input by ignoring its sign.
temp = abs(a)
number = abs(a)
rev = 0
while number > 0:
    rem = number % 10  # Gives last digit
    rev = rev * 10 + rem # Adds last digit to its correct place
    number = number // 10 # Removes last digit
if ( rev == temp ):
    print("Palindrome")
else:
    print("Not Palindrome")