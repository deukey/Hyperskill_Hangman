import random
import re
ATTEMPTS = 8
print("H A N G M A N # {} attempts".format(ATTEMPTS))
records = [0, 0]
while True:
    selected_menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if selected_menu == "play":
        list_of_words = ["python", "java", "swift", "javascript"]
        answer: str = random.choice(list_of_words)
        discovered: str = "-" * len(answer)
        att_left = ATTEMPTS
        input_memory = []
        while att_left > 0:
            print("")
            print(discovered)
            letter = input("Input a letter:")
            if len(letter) != 1:
                print("Please, input a single letter.")
                continue
            else:
                if not letter.isalpha() or not letter.islower():
                    print("Please, enter a lowercase letter from the English alphabet.")
                    continue
            if letter in input_memory:
                print("You've already guessed this letter.")
                continue
            else:
                match = [m.start() for m in re.finditer(letter, answer)]
                input_memory.append(letter)
                if not match:
                    att_left -= 1
                    print("That letter doesn't appear in the word.  # {} attempts".format(att_left))
                    if att_left == 0:
                        records[1] += 1
                        print("You lost!")
                    continue
                else:
                    characters = list(discovered)
                    for k in match:
                        characters[k] = letter
                        discovered = "".join(characters)
                    if discovered == answer:
                        records[0] += 1
                        print("You guessed the word {}!".format(answer))
                        print("You survived!")
                        break
    elif selected_menu == "results":
        print("You won: {} times.".format(records[0]))
        print("You lost: {} times.".format(records[1]))
    elif selected_menu == "exit":
        break