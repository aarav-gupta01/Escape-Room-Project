import random

print("Welcome to the Escape Room!")
# TODO (L5): ask the player for their name and greet them.
name = input("What is your name? ")
print(f"Welcome, {name}!")

#L6
def puzzle():
  correct_password = random.choice(["dragon", "lebron", "abc123"])
  guess = input("What's the password?(lebron, dragon, abc123, bean, tuff, awesome) ")
  
  while guess.lower() != correct_password.lower():
    print("Wrong!")
    guess = input("Try Again ")
  
  print("Correct! You Escaped!")

def puzzle2():
  correct_password = random.choice(["bean", "tuff", "awesome"])
  guess = input("What's the password?(lebron, dragon, abc123, bean, tuff, awesome) ")
  
  while guess.lower() != correct_password.lower():
    print("Wrong!")
    guess = input("Try Again ")
  
  print("Correct! You Escaped!")

#L7
room = [
    "xxxxx",
    "x...x",
    "x.p.x",
    "x.qex",
    "xxxxx",
]

player_row = 1
player_col = 1
puzzle1_solved = False
puzzle2_solved = False

def move(current_row, current_col, direction, room):
  global puzzle1_solved, puzzle2_solved
  if direction == 'up':
    new_row, new_col = current_row - 1, current_col
  elif direction == 'down':
    new_row, new_col = current_row + 1, current_col
  elif direction == 'left':
    new_row, new_col = current_row, current_col - 1
  elif direction == 'right':
    new_row, new_col = current_row, current_col + 1
  else:
    print("Invalid Direction")
    return current_row, current_col
  
  if room[new_row][new_col] == 'x':
    print("Ouch, that's a wall")
    return current_row, current_col
  elif room[new_row][new_col] == 'p':
    if puzzle1_solved == True:
      return new_row, new_col
    puzzle()
    puzzle1_solved = True
    return new_row, new_col
  elif room[new_row][new_col] ==  'q':
    if puzzle2_solved == True:
      return new_row, new_col
    puzzle2()
    puzzle2_solved = True
    return new_row, new_col
  else:
    return new_row, new_col
#L8
def announce_walls(player_row, player_col):
  if room[player_row - 1][player_col] == 'x':#up
    print("There is a wall above you.")
  if room[player_row + 1][player_col] == 'x': #down
    print("There is a wall beneath you.")
  if room[player_row][player_col - 1] == 'x': #left
    print("There is a wall to your left.")
  if room[player_row][player_col + 1] == 'x': #right
    print("There is a wall to your right.")
#L7
while room[player_row][player_col] != 'e' or not puzzle1_solved or not puzzle2_solved:
  announce_walls(player_row, player_col)
  direction = input('Which way? (up/down/left/right): ')
  player_row, player_col = move(player_row, player_col, direction, room)
  print(f"You are at ({player_row}, {player_col})")
print("You Escaped!")


