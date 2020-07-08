import random
import re

print("H A N G M A N")
play_exit = input('Type "play" to play the game, "exit" to quit: ')
if play_exit == "play":

    words = ['java', 'kotlin', 'javascript', 'python']
    word = str(random.choice(words))
    word_modified = '-' * (len(word))
    print()
    print(word_modified)
    trying = 0
    hanged_str = "You are hanged!"
    no_improve_str = "No improvements\n"
    no_such_str = "No such letter in the word\n"
    typed = []

    while trying != 8:

        if trying < 7:
            player_enter = input("Input a letter: ")
            if not player_enter:
                typed.append(player_enter)
                print("You should input a single letter\n")
                print(''.join(word_modified))
            elif player_enter in word:
                typed.append(player_enter)
                if player_enter not in set(word_modified):
                    my_iter = re.finditer(player_enter, word)
                    indexes = [x.start() for x in my_iter]
                    word_modified = list(word_modified)
                    if word_modified.count("-") == 1:
                        for i in indexes:
                            for j in word_modified:
                                word_modified[i] = player_enter
                    else:
                        for i in indexes:
                            for j in word_modified:
                                word_modified[i] = player_enter
                        print()
                        print(''.join(word_modified))
                elif player_enter in set(word_modified):
                    print("You already typed this letter\n")
                    print(''.join(word_modified))
            elif player_enter not in word:
                if len(player_enter) == 0 or len(player_enter) > 1:
                    typed.append(player_enter)
                    print("You should input a single letter\n")
                    print(''.join(word_modified))
                elif player_enter.isupper():
                    typed.append(player_enter)
                    print("It is not an ASCII lowercase letter\n")
                    print(''.join(word_modified))
                elif not player_enter.isalpha():
                    typed.append(player_enter)
                    print("It is not an ASCII lowercase letter\n")
                    print(''.join(word_modified))
                elif player_enter in set(typed):
                    typed.append(player_enter)
                    print("You already typed this letter\n")
                    print(''.join(word_modified))
                else:
                    trying += 1
                    typed.append(player_enter)
                    print(no_such_str)
                    print(''.join(word_modified))

        if trying == 7:
            player_enter = input("Input a letter: ")
            if not player_enter:
                typed.append(player_enter)
                print("You should input a single letter\n")
                print(''.join(word_modified))
            elif player_enter in word:
                typed.append(player_enter)
                if player_enter not in set(word_modified):
                    my_iter = re.finditer(player_enter, word)
                    indexes = [x.start() for x in my_iter]
                    word_modified = list(word_modified)
                    if word_modified.count("-") == 1:
                        for i in indexes:
                            for j in word_modified:
                                word_modified[i] = player_enter
                    else:
                        for i in indexes:
                            for j in word_modified:
                                word_modified[i] = player_enter
                        print()
                        print(''.join(word_modified))
                elif player_enter in set(word_modified):
                    print("You already typed this letter\n")
                    print(''.join(word_modified))
            elif player_enter not in word:
                if len(player_enter) == 0 or len(player_enter) > 1:
                    typed.append(player_enter)
                    print("You should input a single letter\n")
                    print(''.join(word_modified))
                elif player_enter.isupper():
                    typed.append(player_enter)
                    print("It is not an ASCII lowercase letter\n")
                    print(''.join(word_modified))
                elif not player_enter.isalpha():
                    typed.append(player_enter)
                    print("It is not an ASCII lowercase letter\n")
                    print(''.join(word_modified))
                elif player_enter in set(typed):
                    print("You already typed this letter\n")
                    print(''.join(word_modified))
                else:
                    typed.append(player_enter)
                    trying += 1
                    print("No such letter in the word\nYou are hanged!")

        if trying == 8:
            break

        if "-" not in word_modified:
            print(f"You guessed the word {word}!\nYou survived!")
            break
elif play_exit == "exit":
    quit()