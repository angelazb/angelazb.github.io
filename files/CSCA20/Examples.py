##################################################################
# uoft.me/a20-lab7
##################################################################

'''Uncomment each piece of code to see what happens!'''

##################################################################

# Make sure you know the type of your variable!
'''
a = 3
b = "3"
print(a == b)

print(type(a))
print(type(b))

print(a == int(b))
print(str(a) == b)
'''

##################################################################

# Check if a letter is in word
'''
word = "hello"
letter = "e"
if letter in word: # In scratch: word contains letter?
    print("yes")
else:
    print("no")
'''

##################################################################

# Three different ways to print the letters of the word!

# 1. Using a for loop for every letter in the word
'''
word = "hello"
for letter in word:
    print(letter)
'''

# 2. Using a for loop checking the letter of the word based on the index
'''
word = "hello"
for index in range(len(word)): # Repeat (length of word)
    print(word[index])
'''

# 3. Using a while loop until the index reaches the length of the word
'''
index = 0
word = "hello"
while index < len(word): # In scratch: repeat until <index = len(word)>
    print(word[index])
    index += 1
'''

##################################################################

# Play around with lists
'''
list_letters = ['a', 'b', 'c', 'd']

for letter in list_letters:
    print(letter)

list_letters.append('e') # Add element at the end of the list
print(list_letters)

list_letters.remove('d') # Remove specific item
print(list_letters)

list_letters.insert(1, 'Y') # Insert element at an specific position
print(list_letters)

list_letters[1] = 'X' # Replace element at an specific position
print(list_letters)

list_letters.clear() # Delete all the items of the list
print(list_letters)
'''
##################################################################

# Check help(range) to see how it works!
'''
list_numbers = []
for index in range(5):
    list_numbers.append(index)
print(list_numbers)

for index in range(5, 10):
    list_numbers.append(index)
print(list_numbers)
print(list_numbers[1:])
print(list_numbers[3:6])
print(list_numbers[:-1])
'''

##################################################################

# What if you only want to get a range of letters form a word.
'''
word = "Angelaa"
print(word[1:3])
print(word[:-1])
'''