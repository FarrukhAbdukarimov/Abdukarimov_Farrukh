
import random


def guess_number():
    random_number = random.randint(1, 100)
    guessed = False

    while not guessed:
        user_guess = int(input("Угадайте число от 1 до 100: "))

        if user_guess > random_number:
            print("Загаданное число меньше.")
        elif user_guess < random_number:
            print("Загаданное число больше.")
        else:
            guessed = True

    print("Поздравляю! Вы угадали число ", random_number)

