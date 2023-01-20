import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
player = None
while player not in choices:
  player = input("rock, paper, scissors?: ").lower()
if player == computer:
  print("computer: ",computer)
  print("player: ",player)
  print("Tie!")
elif player == "rock":
   print("computer: ",computer)
   print("player: ",player)
   print("Tie!")