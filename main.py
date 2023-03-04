def show(): #создание игрового поля
    print('  | 1 | 2 | 3 |')
    print('---------------')
    for i , row in enumerate(field):
        if i > 0:
            row_str = f"{i} | {' | '.join(row)}"
            print(row_str)
            print('---------------')
    print()


def ask():
    while True:
        cordx = input("   Введите целочисленную координату X (1, 2 или 3) ячейки поля и нажмите 'Enter': ")
        cordy = input("Введите целочисленную координату Y (1, 2 или 3) ячейки поля и нажмите 'Enter': ")

        if not(cordx.isdigit()) or not(cordy.isdigit()):
            print('--- Эх, Семён Семёныч, мы же просили ввести ЧИСЛА :(\nПопробуйте еще раз ---')
            print()
            continue

        x, y = int(cordx), int(cordy)

        if x < 1 or x > 3 or y < 1 or y > 3:
            print("--- Упс, Вы вообще не попали в поле - координаты не в диапазоне от 1 до 3-х :(\nПопробуйте еще раз ---")
            print()
            continue

        if field[x][y-1] != ' ':
            print('--- В домике уже кто-то есть - ячейка занята! Попробуйте еще раз ---')
            print()
            continue

        return x, y

def chek():
    cords = ((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((3,0),(3,1),(3,2)),((1,0),(2,0),(3,0)),((1,1),(2,1),(3,1)),((1,2),(2,2),(3,2)), ((1,0),(2,1),(3,2)),((1,2),(2,1),(3,0))
    for cord in cords:
        symb = []
        for c in cord:
            symb.append(field[c[0]][c[1]])
        if symb == ['X','X','X']:
            print()
            show()
            print ('--- Ура! Выиграл "Х" ! ---')
            return True

        if symb == ['O', 'O', 'O']:
            print()
            show()
            print('--- Ура! Выиграл "O" ! ---')
            return True
    return False


print('--------------------------------')
print('Друзья, приглашаем вас сразиться\nв легендарные "крестики-нолики"!')
print('--------------------------------')
print('Введите целочисленные \nкоординаты ячейки поля, \n\nгде "х" - номер строки, \nа "у" - номер столбца')
print('---------------------')
print(' ЖЕЛАЕМ ВСЕМ ПОБЕДЫ!')
print('---------------------')
print()

print()
field = [[" "] * 4 for i in range(4)]
count = 0
while True:
    count += 1
    print()
    show()
    if count % 2 == 1:
        print('--- КРЕСТИК, Ваш ход :) ---')
        print()
    else:
        print('--- НОЛИК, пожалуйста, ходите :) ---')
        print()

    x, y = ask()

    if count % 2 == 1:
        field[x][y-1] = 'X'
    else:
        field[x][y - 1] = 'O'

    W = chek()
    if W == True:
        break

    if count  == 9:
        print()
        show()
        print('----- БОЕВАЯ НИЧЬЯ! Game over :(')
        break

