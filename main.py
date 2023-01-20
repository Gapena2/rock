import random
from choice import answer

while True:
  choices = ["rock","paper","scissors"]
  computer = random.choice(choices)
  answer(choices,computer)
  play_again = input("play again? (yes/no): ").lower()
  if play_again != "yes":
    break
print("bye!")