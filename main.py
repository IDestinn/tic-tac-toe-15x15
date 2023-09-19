import pyfiglet
import inquirer

from modes.multiplayer import *
from modes.solo import *
from modes.trainmode import *
from modes.custom import *


while True:
    print(pyfiglet.figlet_format("15x15"))

    answer = inquirer.list_input("Выбирите режим", 
                                 choices = ["Игра с ботом", "Играть с другом", 
                                            "Режим тестирования ИИ", "Своя игра", "Выход"])

    if answer == "Игра с ботом":
        start_game_with_bot()
    elif answer == "Играть с другом":
        start_playing_with_friend()
    elif answer == "Режим тестирования ИИ":
        start_training_bots()
    elif answer == "Своя игра":
        custom_game()
    elif answer == "Выход":
        print("Вы вышли из игры. Увидемся!")
        break
    else:
        print("Неверный ввод. Пожалуйста выбирите один из доступных вариантов.")