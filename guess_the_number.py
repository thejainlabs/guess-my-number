import random

print()
print("--------")
print("Welcome to the game!!")
print("I am thinking of a number between 1 and 20")
print("--------")
print()

num = random.randint(1, 20)
counter = 0


while True:
	counter += 1
	guess = int(input("Take a guess: - "))
	print()

	if guess < num:
		print("your guess is too low")
	elif guess > num:
		print("your guess is too high")
	else:
		print(f"Good Job! you guess my number in {counter} tries!")	
		break

	if counter == 6:
		print()
		print(f"You took too many chances, the number i was thinking is {num}")
		break

print("---Game Over---")
print()