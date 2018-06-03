import random, string

# Creating our own functions, 5 separate random letters for 5 separate variables
def generator():
	letter1 = random.choice(string.ascii_lowercase)
	letter2 = random.choice(string.ascii_lowercase)
	letter3 = random.choice(string.ascii_lowercase)
	letter4 = random.choice(string.ascii_lowercase)
	letter5 = random.choice(string.ascii_lowercase)
	name = letter1 + letter2 + letter3 + letter4 + letter5
	return(name)

print(generator())

#Now let's ask user for some input

letter_input_1 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_2 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_3 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_4 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_5 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')