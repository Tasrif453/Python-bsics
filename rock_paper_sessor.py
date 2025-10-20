import random as rd

# Possible moves
r_p_s = ["rock", "paper", "scissor"]

# User input
yc = input("Choose your hand position (Rock, Paper, or Scissor): ").lower()

# Computer random choice
rc = rd.choice(r_p_s)

print(f"Your choice: {yc.capitalize()}")
print(f"Computer chose: {rc.capitalize()}")

# Game logic
if yc == rc:
    print("It's a Draw!")
elif (yc == "rock" and rc == "scissor") or \
     (yc == "paper" and rc == "rock") or \
     (yc == "scissor" and rc == "paper"):
    print("You Win! 🎉")
else:
    print("You Lose 😢")
