import sys
import time
from random import randint

class Monster(object):
  def __init__(self, row, col):
    self.row = row
    self.col = col
  
  def clear(self,board):
    board[self.row][self.col] = "O"
    return board

  def move(self,board):
    newrow = random_row(board)
    newcol = random_col(board)
    if board[newrow][newcol] == "T":  
      monster.move(board) 
    else:
      self.row = newrow
      self.col = newcol
      board[newrow][newcol] = "M"
    return board

class Treasure(object):
  def __init__(self,row,col):
    self.row = row
    self.col = col

# detect presence of Monster and don't overwrite it.
  def place(self,board):
    row = random_row(board)
    col = random_col(board)
    if board[row][col] == "M":  
      treasure.place(board) 
    else:
      self.row = row
      self.col = col
      board[row][col] = "T"
    return board



def directions():
  print("Explore the Haunted Mansion!")
  print("You have to find grandma's Last Will and Testament!")
  print()
  print("Explore by choosing a floor, then opening a door.")
  print()
  print("If you open the door with The Monster, you will die!")
  print("The Monster moves to a random room every turn.")
  print("-------------------------------------")

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
    print("Invalid Entry. Enter 0 to 4.")
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
  print("**ROAR** This room has a Monster! You are eaten!")
  quit()

def win():
  print("You found the Last Will and Testament, you inherit a billion dollars!! WIN!")
  quit()

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

# Main  
# Let's initialize the game board
board = []
dead = False

for x in range(0, 5):
  board.append(["O"] * 5)

# Make an instance of Monster class named Monster
# feed him some random coords to initialize with
# save his position on the board
monster = Monster(random_row(board), random_col(board))
board[monster.row][monster.col] = "M"

# Same for treature. Initialize the object, then place it.
treasure = Treasure(random_row(board), random_col(board))
treasure.place(board)

directions()
spinner = spinning_cursor()

# loop forever.
while not dead:
  print_board(board) #uncomment the print to see the board and cheat/debug
  row = input("Which floor (0 to 4) : ")
  col = input("Which room  (0 to 4) : ")
  if check_valid(row, col):
    print("Opening the door  ", end='')
    for _ in range(20):
      sys.stdout.write(next(spinner))
      sys.stdout.flush()
      time.sleep(0.1)
      sys.stdout.write('\b')
    print()
    row = int(row)
    col = int(col)
    check_monster(row,col)
    check_treasure(row,col)
# if we drop through to this point, the player found an empty room. Move the monster.
  monster.clear(board)
  monster.move(board)
