import random


def fight(weapon, random_weapon):
    if weapon == "Rock":
        print("→" * 100)
    elif weapon == "Scissors":
        print("→" * 100)
    elif weapon == "Paper":
        print("→" * 100)
    else:
        print("your choice is wrong")

    print(random_weapon)

    if weapon == random_weapon:
        print("egalitate, jocul continua")
        print("choose your weapon")
        weapon = input()
        possibility = ["Rock", "Paper", "Scissors"]
        random_weapon = random.choice(possibility)

        fight(weapon, random_weapon)
    if weapon == "Rock" and random_weapon == "Paper":
        print(weapon + " win ")
        return
    if weapon == "Scissors" and random_weapon == "Rock":
        print(random_weapon + " win")
        return

    if weapon == "Paper" and random_weapon == "Rock":
        print(weapon + " win")
        return
    if weapon == "Rock" and random_weapon == "Scissors":
        print(weapon + " win")
        return
    if weapon == "Scissors" and random_weapon == "Paper":
        print(weapon + " win")
        return
    if weapon == "Paper" and random_weapon == "Scissors":
        print(random_weapon + " win")
        return


print('Hi, this is my game')
print('your name is ? : ')
x = input()
print('hellow  ' + x)
print("Do you want to play Rock", "Paper", "Scissors ? ")
print("press y for yes, press n for no")
mod = input()
if mod == "y":
    print("lets go")
    print("START")
    print("Please choose your weapon :)")
    arme = input()
    possibility = ["Rock", "Paper", "Scissors"]
    random_arme = random.choice(possibility)
    fight(arme, random_arme)
elif mod == "n":
    print("maybe next time :)) ")
else:
    print("you need press y for yes, press n for no ")
