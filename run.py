import pyfiglet

from gui.custom import *

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("15x15"))

    answer = inquirer.list_input("Выберите режим",
                                 choices=["C другом", "C ботом",
                                          "Бот против бота", "Своя игра", "Выход"])

    if answer == "C другом":
        start_playing_with_friend()
    elif answer == "C ботом":
        start_game_with_bot()
    elif answer == "Бот против бота":
        start_training_bots()
    elif answer == "Своя игра":
        custom_game()
    elif answer == "Выход":
        print("Вы вышли из игры. До встречи!")
        break
    else:
        print("Неверный ввод. Пожалуйста выберите один из доступных вариантов.")
