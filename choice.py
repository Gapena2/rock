
def answer(choices, computer):
  player = None
  while player not in choices:
    player = input("rock, paper, scissors?: ").lower()
  if player == computer:
    print("computer: ",computer)
    print("player: ",player)
    print("Tie!")
  elif player == "rock":
    if computer == "paper":
     print("computer: ",computer)
     print("player: ",player)
     print("You Lose!")
    if computer == "scissors":
     print("computer: ",computer)
     print("player: ",player)
     print("You Win!")
  elif player == "scissors":
    if computer == "paper":
     print("computer: ",computer)
     print("player: ",player)
     print("You Win!")
    if computer == "rock":
     print("computer: ",computer)
     print("player: ",player)
     print("You Lose!")
  elif player == "paper":
    if computer == "scissors":
     print("computer: ",computer)
     print("player: ",player)
     print("You Lose!")
    if computer == "rock":
     print("computer: ",computer)
     print("player: ",player)
     print("You Win!")
