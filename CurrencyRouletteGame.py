import random
import requests

current_exchange=requests.get("https://api.apilayer.com/exchangerates_data/latest",headers={"apikey":"1KgOIE8oesMQjgqsg28TS1JIDsCSWKO3"})
current_exchange=current_exchange.json()
current_exchange=current_exchange['rates']['ILS']

def get_money_interval(difficulty):
    random_number = random.randint(1, 101)
    print("the sum of many is :", random_number, "how much is worth in shekls")
    bottome_limit = (random_number * current_exchange) - (5 - difficulty)
    up_limit = (random_number * current_exchange) + (5 - difficulty)
    return bottome_limit, up_limit


def get_guess_from_user(difficulty):
    guess_user = float(input("choose your guess"))
    return guess_user


def play(difficulty):
    bottome_limit, up_limit = get_money_interval(difficulty)
    guess_from_user = get_guess_from_user(difficulty)
    if (guess_from_user >= bottome_limit and guess_from_user <= up_limit):
        print("you right ")
        return True
    else:
        print("you lose ")
        return False





