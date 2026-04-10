class Game(): 
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        self.x_score = 0
        self.o_score = 0


    def play_game(self):
            print('welcome to tic tac toe')

    def print_board(self):
        b = self.board
        print(f"""
              A   B   C
          1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
              ----------
          2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
              ----------
          3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        tie = self.tie
        if tie:
            print('Tie game!')
        elif not tie and self.winner:
            print(f"{self.winner} wins the game!")
        else: 
            print(f"It's player {self.turn}'s turn!")


    def render(self):
        self.print_board()
        self.print_message()

    def place_piece(self):
        while True:
            move = input(f'Enter a valid moive (example: A1): ').lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else: 
                print('invalid input') 

    def check_winner(self):
        b = self.board
        winning_combinations = [['a1','b1','c1'], ['a2','b2','c2'], ['a3','b3','c3'], ['a1','a2','a3'], ['b1','b2','b3'], ['c1','c2','c3'], ['a1','b2','c3'], ['c1','b2','a3']]
        for win in winning_combinations: 
            if (b[win[0]] is not None and b[win[0]] == b[win[1]] == b[win[2]]):
                self.winner = self.turn

    def check_tie(self):
        if None not in self.board.values() and self.winner is None:
            self.tie = True

    def switch_turn(self):
        if not self.tie and self.winner is None:
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'     

    def reset_game(self):
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        self.turn = 'X'
        self.tie = False
        self.winner = None

    def record_score(self):
        if self.winner == 'X':
           self.x_score += 1
        if self.winner == 'O':
           self.o_score += 1
        print(f"X score = {self.x_score}, O score = {self.o_score}")


    def play_game(self):
        print("Shall we play a game?")

        while True:
            self.reset_game()

            while self.winner is None and not self.tie:
                self.render()
                self.place_piece()
                self.check_winner()
                self.check_tie()
                self.switch_turn()
        
            self.render()
            self.record_score()

          
            answer = input('Do you want to play again?(Y/N)').lower()
            if answer == 'n': 
                break
                    
game_instance = Game()
game_instance.play_game()
