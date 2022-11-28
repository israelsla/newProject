import random


def generate_number(dificulty):
    return random.randint(1, dificulty)


def get_guess_from_user(dificulty):
    print("please enter a number between 1 to", dificulty)
    guess_of_man = int(input())
    return guess_of_man

def compare_results(secret_number, user_number):
    if secret_number == user_number:
        return True
    else:
        return False


def play(dificulty):
    secret_number = generate_number(dificulty)
    user_number = get_guess_from_user(dificulty)

    if (compare_results(secret_number, user_number)):
        print("you win you guess the correct number ")
    else:
        print("you lose you guess the worng number ")


if __name__ == "__main__":
    play()


