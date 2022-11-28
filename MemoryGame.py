import os
import random
import tkinter
import time


def generate_sequence(difficulty):
    list_number = []
    for i in range(0, difficulty):
        list_number.append(random.randint(1, 101))
    print(list_number)
    # time.sleep(0.7)
    # os.system('cls')
    return list_number


def get_list_from_user(difficulty):
    list_user = []
    print("select the numbers that you remmber ")
    for i in range(0, difficulty):
        number = int(input())
        list_user.append(number)

    return list_user


def is_list_equal(list1, list2):
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False


def play(difficulty):
    list_number = generate_sequence(difficulty)
    list_user = get_list_from_user(difficulty)
    if is_list_equal(list_number, list_user):
        print("you win , you remember well")
    else:
        print("you lose , you dont remember well")
