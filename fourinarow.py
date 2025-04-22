class ConnectFour:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|' + '|'.join(row) + '|')
        print(' ' + ' '.join(map(str, range(self.cols))))

    def drop_piece(self, col):
        if col < 0 or col >= self.cols or self.board[0][col] != ' ':
            return False
        for row in reversed(range(self.rows)):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True
        return False

    def check_winner(self, symbol):
        # Horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col + i] == symbol for i in range(4)):
                    return True
        # Vertical
        for col in range(self.cols):
            for row in range(self.rows - 3):
                if all(self.board[row + i][col] == symbol for i in range(4)):
                    return True
        # Diagonal /
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == symbol for i in range(4)):
                    return True
        # Diagonal \
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == symbol for i in range(4)):
                    return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_full(self):
        return all(self.board[0][col] != ' ' for col in range(self.cols))

    def play_game(self):
        while True:
            self.print_board()
            try:
                col = int(input(f"Player {self.current_player}, choose column (0-{self.cols - 1}): "))
            except ValueError:
                print("Invalid input.")
                continue
            if not self.drop_piece(col):
                print("Column full or invalid. Try again.")
                continue
            if self.check_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            if self.is_full():
                self.print_board()
                print("It's a draw!")
                break
            self.switch_player()

# Main execution
def main():
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        if rows < 4 or cols < 4:
            print("Minimum size for both rows and columns is 4.")
            return
        game = ConnectFour(rows, cols)
        game.play_game()
    except ValueError:
        print("Please enter valid integers for rows and columns.")

main()