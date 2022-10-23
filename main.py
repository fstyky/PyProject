# Игра крестики нолики.
box=[[" "]*3 for i in range(3)]

def Hello():
    print("/////////////////////////\n"
          "// Привествуем в игре  //\n"
          "// крестики Х 0 нолики //\n"
          "/////////////////////////\n")
    show_box()
def show_box():
    print ("    | 0 | 1 | 2 |\n"
           "-----------------\n"
           f"| 0 | {box[0][0]} | {box[0][1]} | {box[0][2]} |\n"
           "-----------------\n"
           f"| 1 | {box[1][0]} | {box[1][1]} | {box[1][2]} |\n"
           "-----------------\n"
           f"| 2 | {box[2][0]} | {box[2][1]} | {box[2][2]} |\n"
           "-----------------")
def moving():

    while True:
        move = input("\n Введите координаты чтобы сделать ход:").split()

        if len(move) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = move

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if not(0 <= x <= 2) or not(0 <= y <= 2):
            print("Введите координаты 0 до 2")
            continue

        if box[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y

def check():
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win:
        symbols = []
        for c in cord:
            symbols.append(box[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Выиграл O!!!")
            return True
    return False

Hello()
hod=1
while True:
    if hod % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = moving()



    if hod % 2 == 1:
        box[x][y] = "X"
    else:
        box[x][y] = "O"

    hod += 1

    show_box()

    if check():
        break

    if hod == 10:
        print(" Ничья!")
        break

