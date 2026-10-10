#python
#Project

#show player rules
print("...")
print("This Is A Guessing Game")
print("...")
print("You have 5 attempts to guess the secret target number.")
print("...")
print("If your guess is higher than the target - the system will say 'Higher!'.")
print("...")
print("If your guess is lower than the target - the system will say 'Lower!'.")
print("...")
print("Each wrong guess subtracts 1 attempt and displays - 'Incorrect!' with your remaining attempts.")
print("...")
print("If you guess correctly, the system will say - 'Correct!' and display your remaining attempts.")
print("...")
print("If you run out of all 5 attempts, - the system will say 'You lost!' and the game ends.")
print("...")
#Pick a hidden number between 1 and 30
import random
random = random.randrange(1,31)
print("Guess the target You have 5 Attempts!")
print("...")
#save the maximum limit of 5  for total  turns.
attempts = 5



# if they put a number lower than the target (target = correct number) output "lower"



# if they put a number higher than the target (target = correct number) output "higher"




# if they fail show output "failed" and show them right number (target they had to get)




#if correct show them the output "correct you got it!"  and there attempts they had left
