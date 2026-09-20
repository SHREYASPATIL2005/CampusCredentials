
a = 121
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