import random

number=random.rand
range(0,100)
guessCheck="wrong"


print("Welcome to Number Guess")


while guessCheck=="wrong":

	response=int(input("Please input a number between 0 and 100:"))

	try:

		val=int(response)

	except ValueError:

		print("This is not a valid integer. Try again...")

		continue

	val=int (response)

	if val<number:

		print("This is lower than actual number. Try again...")

	elif val>number:

		print("This is higher than actual number. Try again...")

	else:

		print("This is the correct number!!!")

		guessCheck="correct"



print("Thank you for playing GUESS THE NUMBER")