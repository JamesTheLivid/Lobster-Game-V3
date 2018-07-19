'''
main.py By James Robinson
Copyright James Robinson 2018
All Rights Reserved
'''

from jamlib import *
from random import randint

# Settings
RIG_WEATHER = [False, "BAD"]    # "GOOD", "BAD"
RIG_HURRICANE = [False, "GOOD"] # "GOOD", "BAD"
START_MONEY = 20
DAYS = {0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday", 4 : "Friday", 5 : "Saturday", 6 : "Sunday" }

DEBUG = True

class player_class():
    def __init__(self):
        global START_MONEY

        self.money = START_MONEY
        self.hotel = False
        self.inshore = -1
        self.outshore = -1

    def in_or_out(self):
        print("How many pots do you want to be inshore and out shore?\n")

        # Loop to make sure the user has a valid selection.
        while 1 < 2:

            self.outshore = integer_input("Outshore: ")
            self.inshore = integer_input(" Inshore: ")

            if self.inshore == -1:
                exit()

            if self.inshore + self.outshore == 6:
                break

            print("\nERROR\n")

class weather_class():

    def __init__(self):
        self.state = False
        self.hurricane = False
        self.bad_streak = 0

    def hurricane_check(self):
        global RIG_HURRICANE

        if self.bad_streak == 3:
            self.hurricane = True

        if RIG_HURRICANE[0] and RIG_HURRICANE[1] == "BAD":
            self.hurricane = True

    def __bad(self):
        self.state = False
        self.bad_streak += 1

        self.hurricane_check()

    def __good(self):
        self.state = True
        self.bad_streak = 0

    def set(self, dice):
        global DEBUG
        global RIG_WEATHER

        if dice == 6:
            self.__bad()

        else:
            self.__good()

        if RIG_WEATHER[0]:
            if RIG_WEATHER[1] == "GOOD":
                self.__good()

            elif RIG_WEATHER[1] == "BAD":
                self.__bad()


        if DEBUG:
            print("weather.state = {}".format(self.state))

    def report(self):
        # Prints title
        print_file("Weather//main")

        # Prints good or bad
        if self.state:
            print_file("Weather//good")

        else:
            print_file("Weather//bad")

        # Prints streak
        print_file("Weather//Streak//{}".format(self.bad_streak))

        # Print hurricane
        if self.hurricane:
            print_file("Weather//hur")

class lobgame():

    def __init__(self, player = player_class(), weather = weather_class()):
        global RIG_WEATHER
        global DEBUG

        self.player = player
        self.weather = weather
        self.rig_weather = RIG_WEATHER

        self.good_weather = True
        self.dice = 0
        self.hurricane = False
        self.bad_weather_streak = 0
        self.day = -1
        self.length_of_game = 40

    def weekday(self):
        if self.day == 5 or self.day == 6:
            return False
        else:
            return True

    def calculate_earnings(self):
        if self.weather.state:
            money = (self.player.inshore * 3) + (self.player.outshore * 5)

        else:
            money = (self.player.inshore * 5) - (self.player.outshore * 6)

        return money

    def new_day(self):
        global DAYS

        # Changes day
        self.day += 1
        print("You wake up to find that you have {} in your bank account safe from the government!".format(money_format(self.player.money)))

        if self.weekday():
            # Message announcing day
            print("It's {}! Time for slave labor!".format(DAYS[self.day % 7]))

            # Rolls the dice
            self.dice = randint(1, 6)
            if DEBUG:
                print("lobgame.dice = {}".format(self.dice))

            # Ask for hotel
            if string_input("Do you want to stay at the hotel today? ")[0] == "n":

                # Gets in/out from player
                self.player.in_or_out()

                # Gets weather report
                if self.weather.bad_streak == 3:
                    self.weather.bad_streak = 0

                self.weather.set(self.dice)
                self.weather.report()

                # Calculate earnings
                self.calculate_earnings()

            # Yes to hotel
            else:
                self.player.money += 15

        # Weekend day
        else:
            print("It's {}! Time to rest!")

            if self.weather.bad_streak == 3:
                self.weather.bad_streak = 0

            self.weather.set(self.dice)
            self.weather.report()


def money_format(money):
    if money <= 0:
        return "-£{}".format(money)

    else:
        return "£{}".format(money)


def main():
    print_file("intro")

    game = lobgame()

    # Main game
    while 1 < 2:

        while 1 < 3:

            game.new_day()

        break

if __name__ == "__main__":
    main()