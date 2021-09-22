import random

rnum = 0
money = 100
bet = 0
next = True
red = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
black = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
number = 0
colansw = "something"
numansw = 37
gamemode = 0
allow = False
want = "yes"

var = "akarmi"

def tobet():
    global allow, bet, money
    allow = False
    while not allow:
        bet = int(input("Place your bet. "))
        if bet <= money and bet > 0:
            allow = True
        elif bet > money:
            print("Invalid quantity.")


def continued():
    global want, next
    want = input("Do you want to continue the game? (yes or no): ")
    if want == "no":
        next = False


while next and money > 0:

    rnum = random.randint(1, 37)

    # 1=red 2=black 3=green

    if rnum <= 18:
        rnum = 1
        number = random.choice(red)
    elif rnum > 18 and rnum <= 36:
        rnum = 2
        number = random.choice(black)
    else:
        rnum = 3
    print("Now you have", money, "money.")
    gamemode = int(input("What would you bet on?: (1=color 2=number): "))

    if gamemode == 1:

        colansw = input("Coose a color. (red, black or green): ")
        if colansw == "red":
            colansw = 1
        elif colansw == "black":
            colansw = 2
        elif colansw == "green":
            colansw = 3

        tobet()

        if colansw == rnum:
            if colansw == 3:
                money = money + (bet * 35)
            else:
                money += bet
            print("Congratulation! You win! Now you have", money, "money.")
            continued()
        else:
            money -= bet
            print("Sorry you didn't win. Now you have", money, "money.")

            if rnum == 1:
                rnum = "red"
            elif rnum == 2:
                rnum = "black"
            else:
                rnum = "green"

            print("The correct color is", rnum)

            if money > 0:
                continued()

    elif gamemode == 2:

        numansw = input("Coose a number between 1 and 36: ")

        tobet()

        if numansw == number:
            money = money + (bet * 35)
            print("Congratulation! You win! Now you have", money, "money.")
            continued()
        else:
            money -= bet
            print("Sorry you didn't win. Now you have", money, "money.")
            print("The correct number is", number)
            if money > 0:
                continued()

print("Game over.")
print("You have", money, "money.")
