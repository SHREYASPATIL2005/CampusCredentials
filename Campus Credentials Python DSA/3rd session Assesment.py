# Given:names = ["Ram", "Sita", "Amit", "Neha"]Create a list containing the length of each name.
Names = ["Ram", "Sita", "Amit", "Neha"]
Name_lengths = [len(name) for name in Names]
print(Name_lengths)


# Given a list of names, create a list containing names whose length is greater than 4. Use above list
Names = ["Ram", "Sita", "Amit", "Neha", "Ramesh", "Siddharth", "Anjali"]
print([name for name in Names if len(name) > 4])

# Given:words = ["apple", "banana", "cat", "dog", "elephant"] list containing words that starts with a
words = ["apple", "banana", "cat", "dog", "elephant"]
print([word for word in words if word.startswith('a')])

# Create a list from 1 to 50 where:numbers divisible by 3 are includedother numbers are ignored.
list_div_by_3 = [num for num in range(1,51) if num % 3 ==0]
print(list_div_by_3)

# Create a list from 1 to 20 where:even numbers → "Even"odd numbers → "Odd"
list_even_odd = ["Even" if num % 2 == 0 else "Odd" for num in range(1,21)]
print(list_even_odd)

