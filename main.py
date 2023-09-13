from graphics.menu import *
from modes.multiplayer import *
from modes.solo import *
from modes.trainmode import *

while True:
    display_start_menu()
    choice = input("Выбирите режим: ")

    if choice == "1":
        start_game_with_bot()
    elif choice == "2":
        start_playing_with_friend()
    elif choice == "3":
        start_training_bots()
    elif choice == "4":
        print("Вы вышли из игры. Увидемся!")
        break
    else:
        print("Неверный ввод. Пожалуйста выбирите один из доступных вариантов.")