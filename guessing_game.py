import random

random_number = random.randint(1, 10) # numbers 1 - 10

#handle user guesses
# if they guess correct, tell them they won
# otherwise tell them if they are too high or too low

#Bonus - let player play again if they want




while True: #message != random_number: keeps going forever until hits break
	message = int(input("Guess a number between 1 to 10: "))
	if message < random_number:
		message = print(f"{message} is too low. Try again")
	elif message > random_number:
		message = print(f"{message} is too high. Try again")
	else:	
		print(f"{message} is correct!")
		play_again = input("Do you want to play again? y/n: ")
		if play_again == "y":
			random_number = random.randint(1, 10)
			message = None
		else:
			print("Thank you for playing!")
			break