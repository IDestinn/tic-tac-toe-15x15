import os
from modes.multiplayer import start_playing_with_friend


def custom_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            rows = int(input("Введите количество строк: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if 0 < rows < 21:
                break
            else:
                print("Запишите число от 1 до 20")
        except ValueError:
            print("Запишите число от 1 до 20")

    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            cols = int(input("Введите количество столбцов: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if 0 < cols < 21:
                break
            else:
                print("Запишите число от 1 до 20")
        except ValueError:
            print("Запишите число от 1 до 20")

    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        try:
            need_to_win = int(input("Введите количество символов в ряд необходимое для победы: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            if 0 < need_to_win <= rows or need_to_win <= cols:
                break
            else:
                print("Число должно быть меньше или равно числу рядов или столбцов")
        except ValueError:
            print("Запишите число")

    os.system('cls' if os.name == 'nt' else 'clear')

    start_playing_with_friend(rows, cols, need_to_win)
