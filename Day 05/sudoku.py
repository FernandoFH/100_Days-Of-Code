"""
Determine si un tablero de Sudoku de 9 x 9 es válido. 
Solo las celdas llenas deben validarse de acuerdo con las siguientes reglas:

[X] Chequear que el tablero introducido sea un tablero 9x9 
[X] Cada fila debe contener los dígitos 1-9 sin repetición.
[X] Cada columna debe contener los dígitos 1-9 sin repetición.
[ ] Cada uno de los nueve subcuadros de 3 x 3 de la cuadrícula debe contener 
"""

board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

class ValidateSudoku:
    def __init__(self, board) -> None:
        self.board = board
        self.invert_list = list()


    def general_validation(self):
        #assert
        assert len(self.board) == 9, "El tablero debe ser de 9x9"
        for row in self.board:
            assert len(row) == 9, "El tablero debe ser de 9x9"


    def row_validation(self, checklist='general_board'):
        if checklist == 'general_board':
            checklist = self.board
        for row in checklist:
            for elemento in row:
                if elemento != ".":
                    assert row.count(elemento) == 1, "El tablero ingresado no es válido"


    def column_validation(self):
        for column_index in range(0,9):
            for row_index in range(0,9):
                self.invert_list.append(self.board[row_index][column_index])
            
            self.row_validation([self.invert_list])
            
            self.invert_list.clear()


    def sub_square_validation(self):
         self.square_3_validation(0,3)
         self.square_3_validation(3,6)
         self.square_3_validation(6,9)
         

    def square_3_validation(self, start_row, end_row):
        self.invert_list.clear()
        for column_index in range(0,9):
            if column_index % 3 == 0:
                self.invert_list.clear()
            for row_index in range(start_row,end_row):
                self.invert_list.append(self.board[row_index][column_index])
                if len(self.invert_list) == 9:
                    self.row_validation([self.invert_list])

# Instanciar Objeto 
if __name__ == '__main__':
    validate = ValidateSudoku(board)
    validate.general_validation()
    validate.row_validation()
    validate.column_validation()
    validate.sub_square_validation()
    print("El tablero ingresado es válido")