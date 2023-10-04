import pyfiglet
import inquirer

from modes.solo import *
from modes.trainmode import *
from modes.custom import *

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("15x15"))

    answer = inquirer.list_input("Выберите режим",
                                 choices=["Игра с ботом", "Играть с другом",
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
        print("Вы вышли из игры. До встречи!")
        break
    else:
        print("Неверный ввод. Пожалуйста выберите один из доступных вариантов.")
