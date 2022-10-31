import random

prompt = """
===========================
(1) Rock 
(2) Paper
(3) Scissors
===========================
Choose one:
"""

player = input(prompt)

while player != "1" and player != "2" and player != "3":
    print("\n[ERR] Please enter an integer between 1 and 3.")
    player = input(prompt)

computer = random.randint(1,3)

player = int(player)

map = {1: "Rock", 2: "Paper", 3: "Scissors"}

if player == computer:
    winner = "Tie"
elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    winner = "Computer"
elif (player == 2 and computer == 1) or (player == 3 and computer == 2) or (player == 1 and computer == 3):
    winner = "Player"

print("===========================")
print("You chose: {}".format(map[player]))
print("Computer chose: {}".format(map[computer]))
print("Winner: {}".format(winner))
print("===========================")
