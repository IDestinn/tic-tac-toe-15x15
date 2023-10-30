"""Этот файл предназначен для запуска основной программы.
Чтобы запустить проект, нажмите на файл run.py два раза, или напишите в терминале "python run.py".
"""
import os
import pyfiglet
import inquirer
from gui.custom import custom_game
from modes import start_game_with_bot, start_training_bots, start_playing_with_friend

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана
    print(pyfiglet.figlet_format("Tic-Tac-Toe"))  # Вывод названия программы

    # Вывод вариантов работы программы и запись ответа пользователя
    answer = inquirer.list_input("Выберите режим",
                                 choices=["C другом", "C ботом",
                                          "Бот против бота", "Своя игра", "Выход"])

    # Воспроизведения выбранного режима игры
    match answer:
        case "C другом":
            start_playing_with_friend()
        case "C ботом":
            start_game_with_bot()
        case "Бот против бота":
            start_training_bots()
        case "Своя игра":
            custom_game()
        case "Выход":
            print("Вы вышли из игры. До встречи!")
            break
        case _:
            print("Неверный ввод. Пожалуйста выберите один из доступных вариантов.")
