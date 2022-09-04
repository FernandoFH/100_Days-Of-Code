"""[worldle.py]
_ _ _ _ _ _ 
_ _ _ _ _ _ 
_ _ _ _ _ _ 
_ _ _ _ _ _ 
_ _ _ _ _ _ 
_ _ _ _ _ _ 

palabra - intento -> Gana!
letra in palabra -> Ayuda!
letra no in palabra -> No existe!
"""
colors = {
    'green': '\033[92m',
    'red': '\033[91m',
    'yellow': '\033[93m',    
    'end': '\033[0m'
}

def color_letter(letter, color):
    return colors[color] + letter + colors['end']


# init game 
win = False
word = "radios"
len_word = len(word)

board = []
for i in range(len_word):
    board.append(["_"] * len_word)

game_loop_count = 0
# game loop
while (not win) and (game_loop_count < len_word):
    text = input("Ingrese palabra: ")
    while len_word != len(text):
        print(f"La palabra debe tener {len_word} letras")
        text = input("Ingrese palabra: ")
    
    # win condition
    if word == text:
        board[game_loop_count] = [color_letter(l, 'green') for l in text]
        win = True
    # letter in word
    else:
        test_line = []
        for j in range(len(text)):
            if text[j] == word[j]:
                test_line.append(color_letter(text[j], 'green'))
            elif text[j] in word:
                test_line.append(color_letter(text[j], 'yellow'))
            else:
                test_line.append(color_letter(text[j], 'red'))
        
        board[game_loop_count] = test_line   


    # print board
    for i in range(len_word):
        print(" ".join(board[i]))

    game_loop_count += 1


if win:
    print("Ganaste!")
else:
    print("Perdiste!")