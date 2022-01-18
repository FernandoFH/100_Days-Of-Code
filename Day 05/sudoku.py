"""
Determine si un tablero de Sudoku de 9 x 9 es válido. 
Solo las celdas llenas deben validarse de acuerdo con las siguientes reglas:

[X] Chequear que el tablero introducido sea un tablero 9x9 
[X] Cada fila debe contener los dígitos 1-9 sin repetición.
[ ] Cada columna debe contener los dígitos 1-9 sin repetición.
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


    def general_validation(self):
        #assert
        assert len(self.board) == 9, "El tablero debe ser de 9x9"
        for row in self.board:
            assert len(row) == 9, "El tablero debe ser de 9x9"


    def row_validation(self):
        for row in self.board:
            for elemento in row:
                if elemento != ".":
                    assert row.count(elemento) == 1, "La fila no puede contener numeros repetidos."



# Instanciar Objeto 
sudoku = ValidateSudoku(board)
sudoku.general_validation()
sudoku.row_validation()