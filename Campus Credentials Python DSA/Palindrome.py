
a = 121
temp = a
rev = 0
sum = 0
while a > 0:
    rem = a % 10  # Gives last digit
    sum += rem # For addition
    print(rem)
    rev = rev * 10 + rem # Adds last digit to its correct place
    a = a // 10 # Removes last digit
    print(a)
    print(rev)
if ( rev == temp ):
    print("Pallindrome")
else:
    print("Not Palindrome")