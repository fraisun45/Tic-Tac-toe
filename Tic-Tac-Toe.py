
"""The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw."""
positions = [1,2,3,4,5,6,7,8,9]

def main (col,row):
    rows = '\n'+"|"  * row
    columns = "-+-" * col

    return (columns + rows) 

def maping(array):
    for i in array:
        print(str(i) + main(2,1)) 

maping(positions)




while True:
    ready = input("Are you ready? When you are, input 'yes'.")
    if ready.lower() == 'yes': break

    def printboard(n, board):
        print() #print board in ranks of n length; n given later
        boardbyrnk = [board[ind:ind+n] for ind in range(0,n**2,n)]
        for rank in range(n):
          rn = f"{n-rank:02d}" #pads with a 0 if rank number < 10
          print(f"{rn}|{'|'.join(boardbyrnk[rank])}|") #with rank#'s
        print("  ",end="") #files at bottom of board
        for file in range(97,n+97):
            print(f" {chr(file)}", end="")
        print()

    def sqindex(prompt, n, board, syms): #takes input & returns index
        #ss is a list/array of all possible square names
        ss = [chr(r+97)+str(f+1) for r in range(n) for f in range(n)]
        while True: #all bugs will cause input to be taken for same turn
            sq = input(prompt)
            if sq not in ss: print("Square doesn't exist!"); continue
            #the index is found by multiplying rank and adding file #'s
            index = n*(n-int(sq[1:])) + ord(sq[0])-97
            if board[index] in syms: #ensure it contains ' '
              print("The square must be empty!"); continue
            return index

    def checkwin(n, w, board, sm): #TODO
      #check rows, columns and diagonals in terms of n and w;
      #presumably return True if each case is met
      return False

    ps = ["Player 1", "Player 2"]; syms = ['X', 'O']
    #determines number of symbols in a row needed to win later on
    c = {3:[3,3],4:[4,6],5:[7,13],6:[14,18],7:[19,24],8:[25,26]}
    goagain = True
    while goagain:
      #decide on board size
      while True:
        try: n=int(input(f"\n{ps[1]}, how long is the board side? "))
        except ValueError: print("Has to be an integer!"); continue
        if not(2<n<27): print("Has to be from 3 to 26."); continue
        break
      board = (n**2)*" " #can be rewritten around a square's index

      for num in c:
        if c[num][0] <= n <= c[num][1]: w = num; break
      print(f"You'll have to get {w} symbols in a row to win.")

      for tn in range(n**2): #tn%2 = 0 or 1, determining turn order
        printboard(n, board)
        pt = ps[tn%2]
        sm = syms[tn%2]
        prompt = f"{pt}, where do you place your {sm}? "
        idx = sqindex(prompt, n, board, syms)
        #the index found in the function is used to split the board string
        board = board[:idx] + sm + board[idx+1:]
        if checkwin(n, w, board, sm):
          printboard(n, board); print('\n' + pt + ' wins!!\n\n')
          break
        if board.count(" ") == 0:
          printboard(n, board); print("\nIt's a draw!")

      while True: #replay y/n; board size can be redetermined
        rstorq = input("Will you play again? Input 'yes' or 'no': ")
        if rstorq in ['yes', 'no']:
          if rstorq == 'no': goagain = False
          break
        else: print("Please only input lowercase 'yes' or 'no'.")

    print("Thanks for playing!")

"""The program must have a comment with assignment and author names.
The program must have at least one if/then block.
The program must have at least one while loop.
The program must have more than one function.
The program must have a function called main."""

"""Suggestions
Make the game in any way you like. A few ideas are as follows.

Enhanced input validation with user-friendly messages.
Enhanced game over messages (x's, o's or draw).
Enhanced board size (4x4, 5x5, 6x6 grid, or user selected!)
Enhanced game display (different colors for each player)"""
