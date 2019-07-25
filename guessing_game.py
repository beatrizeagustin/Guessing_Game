import random

random_number = random.randint(1, 10) # numbers 1 - 10

#handle user guesses
# if they guess correct, tell them they won
# otherwise tell them if they are too high or too low

#Bonus - let player play again if they want

message = int(input("Guess a number between 1 to 10: "))


while message != random_number:
	if message < random_number:
		message = int(input(f"{message} is too low. Try again: "))
	if message > random_number:
		message = int(input(f"{message} is too high. Try again: "))
print(f"{message} is correct!")