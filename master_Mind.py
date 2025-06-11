#!/bin/python3
# MasterMind - Kleuren & Nummers versie
# by ICTROCN
# v1.02
# 4-6-2025
# Last mod by DevJan: kleurenversie + keuzemenu toegevoegd

import random


def generate_number_code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]


def generate_color_code(length=4):
    return [random.choice(possibleColors) for _ in range(length)]


possibleColors = ["Blue", "Purple", "Red", "Orange", "Yellow", "Green"]


def get_Feedback(secret, guess):
    secret_lower = [s.lower() for s in secret]
    guess_lower = [g.lower() for g in guess]

    black_Pegs = sum(s == g for s, g in zip(secret_lower, guess_lower))

    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret_lower, guess_lower):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(
        min(secret_Counts.get(c, 0), guess_Counts.get(c, 0)) 
        for c in guess_Counts
        )

    return black_Pegs, white_Pegs


def show_Secret(secret):
    print("De geheime code was:", ', '.join(secret))


def play_number_mode():
    print("Welkom bij Mastermind met cijfers!")
    print(
        "Raad de 4-cijferige code. Elk cijfer is van 1 t/m 6. Je hebt 10 pogingen."
        )
    secret_Code = generate_number_code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Poging {attempt}: ").strip()

            if guess.lower() == "cheat":
                password = input("Voer cheat-wachtwoord in: ").strip()
                if password == "admin":
                    show_Secret(secret_Code)
                else:
                    print("Verkeerd wachtwoord. Cheat geweigerd.")
                continue

            valid_Guess = len(guess) == 4 and all(c in "123456" for c in guess)
            if not valid_Guess:
                print(
                    "Ongeldige invoer. Voer precies 4 cijfers in van 1 t/m 6."
                    )

        guess_list = list(guess)
        black, white = get_Feedback(secret_Code, guess_list)
        print(
            f"Black pegs (juiste plek): {black}, "
            f"White pegs (verkeerde plek): {white}"
        )


        if black == 4:
            print(f"Gefeliciteerd! Je hebt de code geraden: 
            {''.join(secret_Code)}")
            return


    print(f"Helaas, je hebt alle pogingen gebruikt. De code was: {''.join(secret_Code)}")


def play_color_mode():
    print("Welkom bij Mastermind met kleuren!")
    print(f"Raad de juiste volgorde van 4 kleuren. Kies uit: 
    {', '.join(possibleColors)}")
    print(
        "Typ je kleuren gescheiden door spaties (bijv: Red Blue Yellow Green)"
        )
    secret_Code = generate_color_code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        valid_Guess = False
        guess = []

        while not valid_Guess:
            user_input = input(f"Poging {attempt}: ").strip()

            if user_input.lower() == "cheat":
                password = input("Voer cheat-wachtwoord in: ").strip()
                if password == "admin":
                    show_Secret(secret_Code)
                else:
                    print("Verkeerd wachtwoord. Cheat geweigerd.")
                continue

            guess = user_input.split()
            guess = [color.capitalize() for color in guess]

            if len(guess) != 4 
            or not all(color in possibleColors for color in guess):
                print(
                    "Ongeldige invoer. Voer exact 4 kleuren in uit de lijst (hoofdletterongevoelig)."
                    )
            else:
                valid_Guess = True

        black, white = get_Feedback(secret_Code, guess)
        print(f"Zwarte pionnen: {black}, Witte pionnen: {white}")

        if black == 4:
            print(f"Goed gedaan! Je raadde de code: {', '.join(secret_Code)}")
            return

    print(f"Helaas! De juiste code was: {', '.join(secret_Code)}")


def play_Mastermind():
    print("Welkom bij Mastermind!")
    mode = ""
    while mode not in ["colors", "numbers"]:
        mode = input(
            "Wil je spelen met kleuren of cijfers? Typ 'colors' of 'numbers': "
            ).strip().lower()

    if mode == "colors":
        play_color_mode()
    else:
        play_number_mode()


if __name__ == "__main__":
    again = 'Y'
    while again.upper() == 'Y':
        play_Mastermind()
        again = input("Nog een keer spelen? (Y/N): ").strip().upper()
