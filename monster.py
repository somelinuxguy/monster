from random import randint

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)


def check_valid(row, col):
  try:
    int(row)
    int(col)
  except ValueError:
    print("No. You need to use numbers.")
    return False

  if (int(row) not in range(5)) or (int(col) not in range(5)):
    print("Invalid Entry. Your house has 5 floors and five rooms, enter 0 to 4.")
    return False
  else:
    return True


def check_monster(row, col):
    if board[row][col] == "M":
        lose()
    else:
        print("The room is not haunted...")

def check_treasure(row, col):
    if board[row][col] == "T":
        win()
    else:
        print("What you seek is not in this room. Keep looking.\n")

def lose():
  print("You are eaten. LOSE!")
  quit()

def win():
  print("You found the Last Will and Testament of Grandma, you get all her stuff!! WIN!")
  quit()

# Main  
# Let's initialize the game board
board = []
dead = False

for x in range(0, 5):
  board.append(["O"] * 5)

# Place the first Monster
board[random_row(board)][random_col(board)] = "M"
# Now place the treasure
board[random_row(board)][random_col(board)] = "T"

print("You find yourself in a five story haunted mansion, five rooms per floor.")
print("You have to find grandma's Last Will and Testament!")
print("If you open the door with a monster, you will die.")
print("The monster moves to a random room every turn.\n\n")

# Uncomment to debug
# print_board(board)

# loop forever.
# at some point I might write another function
# that returns dead = True but for now that is not needed.
while not dead:
  row = input("Which floor? ")
  col = input("Which room ? ")
  if check_valid(row, col):
    print("Opening the door.")
    row = int(row)
    col = int(col)
    check_monster(row,col)
    check_treasure(row,col)
