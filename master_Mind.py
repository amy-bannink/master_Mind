# #!/bin/python3
# # MasterMind
# # by ICTROCN
# # v1.01
# # 15-8-2024
# # Last mod by DevJan : added loop for replay
# print("MasterMind")

# import random
# #comment toegevoegd


# def generate_Code(length=4, digits=6):
#     return [str(random.randint(1, digits)) for _ in range(length)]

# def generate_color_code(length=4):
#     possibleColors = ["Blue", "Purple", "Red", "Orange", "Yellow", "Green"]
#     return [random.choice(possibleColors) for _ in range(length)]


# def get_Feedback(secret, guess):
#     black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
#     # Count whites by subtracting black and calculating min digit frequency match
#     secret_Counts = {}
#     guess_Counts = {}

#     for s, g in zip(secret, guess):
#         if s != g:
#             secret_Counts[s] = secret_Counts.get(s, 0) + 1
#             guess_Counts[g] = guess_Counts.get(g, 0) + 1

#     white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
#     return black_Pegs, white_Pegs

# def show_Secret(mystery):
#     print(mystery)

# def play_Mastermind():
#     print("Welcome to Mastermind!")
#     print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
#     secret_Code = generate_Code()
#     attempts = 10

#     for attempt in range(1, attempts + 1):
#         guess = ""
#         valid_Guess = False
#         while not valid_Guess:
#             guess = input(f"Attempt {attempt}: ").strip()

#             if guess == "cheat":
#                 password = input("Enter cheat password: ").strip()
#                 if password == "admin":
#                     show_Secret(secret_Code)
#                 else:
#                     print("Incorrect password. Cheat mode denied.")
#                 continue  # Terug naar input vragen

#             valid_Guess = len(guess) == 4 and all(c in "123456" for c in guess)
#             if not valid_Guess:
#                 print("Invalid input. Enter 4 digits, each from 1 to 6.")



#         black, white = get_Feedback(secret_Code, guess)
#         print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

#         if black == 4:
#             print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
#             return

#     print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

# if __name__ == "__main__":
#     again = 'Y'
#     while again == 'Y' :
#         play_Mastermind()
#         again  = input (f"Play again (Y/N) ?").upper()

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
    # Normaliseer input naar lowercase (voor kleurenversie)
    secret_lower = [s.lower() for s in secret]
    guess_lower = [g.lower() for g in guess]

    black_Pegs = sum(s == g for s, g in zip(secret_lower, guess_lower))

    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret_lower, guess_lower):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(c, 0), guess_Counts.get(c, 0)) for c in guess_Counts)

    return black_Pegs, white_Pegs

def show_Secret(secret):
    print("De geheime code was:", ', '.join(secret))

def play_number_mode():
    print("Welkom bij Mastermind met cijfers!")
    print("Raad de 4-cijferige code. Elk cijfer is van 1 t/m 6. Je hebt 10 pogingen.")
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
                print("Ongeldige invoer. Voer precies 4 cijfers in van 1 t/m 6.")

        guess_list = list(guess)
        black, white = get_Feedback(secret_Code, guess_list)
        print(f"Black pegs (juiste plek): {black}, White pegs (verkeerde plek): {white}")

        if black == 4:
            print(f"Gefeliciteerd! Je hebt de code geraden: {''.join(secret_Code)}")
            return

    print(f"Helaas, je hebt alle pogingen gebruikt. De code was: {''.join(secret_Code)}")

def play_color_mode():
    print("Welkom bij Mastermind met kleuren!")
    print(f"Raad de juiste volgorde van 4 kleuren. Kies uit: {', '.join(possibleColors)}")
    print("Typ je kleuren gescheiden door spaties (bijv: Red Blue Yellow Green)")
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
            guess = [color.capitalize() for color in guess]  # Normaliseer hoofdletters

            if len(guess) != 4 or not all(color in possibleColors for color in guess):
                print("Ongeldige invoer. Voer exact 4 kleuren in uit de lijst (hoofdletterongevoelig).")
            else:
                valid_Guess = True

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (juiste kleur & plek): {black}, White pegs (juiste kleur, verkeerde plek): {white}")

        if black == 4:
            print(f"Goed gedaan! Je raadde de code: {', '.join(secret_Code)}")
            return

    print(f"Helaas! De juiste code was: {', '.join(secret_Code)}")

def play_Mastermind():
    print("Welkom bij Mastermind!")
    mode = ""
    while mode not in ["colors", "numbers"]:
        mode = input("Wil je spelen met kleuren of cijfers? Typ 'colors' of 'numbers': ").strip().lower()

    if mode == "colors":
        play_color_mode()
    else:
        play_number_mode()

if __name__ == "__main__":
    again = 'Y'
    while again.upper() == 'Y':
        play_Mastermind()
        again = input("Nog een keer spelen? (Y/N): ").strip().upper()
