# feature show one board at a time

# using list as a data structure since access and change elements in it
board = ["   " for i in range(9)]


# creating a function which prints the actual board
def print_board():
  row1 = f"|{board[0]}|{board[1]}|{board[2]}|"
  row2 = f"|{board[3]}|{board[4]}|{board[5]}|"
  row3 = f"|{board[6]}|{board[7]}|{board[8]}|"

  print(f"\n{row1}\n{row2}\n{row3}\n")


# creating a function player move  
def player_move(icon):
  if icon == " X ":
    number = 1
  elif icon == " O ":
    number = 2

  print(f"Your turn player {number}")

  choice = int(input("Enter your move (1-9): ").strip())
  if board[choice -1] == "   ":
    board[choice -1] = icon
  else:
    print(f"\nThat space is already taken!")
  


# creating a function to define victory    
def victory(icon):

  if (board[0] == icon and board[1] == icon and board[2] == icon) or \
     (board[3] == icon and board[4] == icon and board[5] == icon) or \
     (board[6] == icon and board[7] == icon and board[8] == icon) or \
     (board[0] == icon and board[3] == icon and board[6] == icon) or \
     (board[1] == icon and board[4] == icon and board[7] == icon) or \
     (board[2] == icon and board[5] == icon and board[8] == icon) or \
     (board[0] == icon and board[4] == icon and board[8] == icon) or \
     (board[2] == icon and board[4] == icon and board[6] == icon):
    return True
  else:
    return False


# creating a function to check when the game end at a draw  
def is_draw():
  if "   " not in board:
    return True
  else:
    return False


# main logic block
while True:
  print_board()
  player_move(" X ")
  print_board()
  if victory(" X "):
    print("X Wins! Congratulations!")
    break
  elif is_draw():
    print("Its a draw!")
    break
  player_move(" O ")
  if victory(" O "):
    print_board()
    print("O Wins! Congratulations!")
    break
  elif is_draw():
    print("Its a draw!")
    break

  




