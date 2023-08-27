
# I ❤️ trig!!!!

import random
from os import system
from time import sleep
from fractions import Fraction
from math import sin, cos, tan, pi

def trig(problems):

    functions =  {"sin": sin, "tan": tan, "cos": cos}

    angles    =  {"π/6": pi/6, "π/4": pi/4,  "π/3": pi/3, "π/2": pi/2,
                 "2π/3": (2*pi)/3, "3π/4": (3*pi)/4, "5π/6": (5*pi)/6,
                  "π": pi,"7π/6": (7*pi)/6, "5π/4": (5*pi)/4,
                  "4π/3":(4*pi/3), "3π/2": (3*pi)/2, "5π/3": (5*pi)/3,
                  "7π/4":(7*pi)/4, "11π/6":(11*pi)/6,
                  "2π": 2*pi, "0π": 0*pi}

    answers = {7836263351624663/9007199254740992: "√3/2", -7836263351624663/9007199254740992: "-√3/2",
              -799388933858263/1125899906842624: "-√2/2",  799388933858263/1125899906842624: "√2/2",
              -5224175567749775/9007199254740992: "-√3/3", 5224175567749775/9007199254740992: "√3/3",
              -3895613677675479/2251799813685248: "-√3", 3895613677675479/2251799813685248: "√3",
              5443746451065123: "undefined", 16331239353195370: "undefined"}

    correct = 0
    wrong   = 0
    current_streak = 0
    max_streak = 0

    for i in range(problems):
        system("clear")
        randnom_angle   = random.choice(list(angles.keys()))
        random_function = random.choice(list(functions.keys()))
        user_answer     = str(input(f"\nWhat is the value of {random_function}({randnom_angle})?"))
        answer          = Fraction(round(functions[random_function](angles[randnom_angle]), 2))

        if answer in answers:
            answer = answers[answer]

        if user_answer == str(answer): # RIGHT ANSWER
            correct += 1
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak

            sleep(1)
            print("\n✅ Correct!")
            if current_streak > 2:
                print("🔥", current_streak)

            sleep(0.5)
            tmp = input("\nENTER to continue...")

        else: # WRONG ANSWER
            if current_streak > 2:
                print("🔥 0")
            wrong += 1
            current_streak = 0
            sleep(1)
            print("\n❌ The answer is:", answer)
            sleep(0.5)
            tmp = input("\nENTER to continue...")
        print("")

    system("clear")
    print("\n🔥", max_streak, "|", "✅", correct, "|", "❌", wrong, "\n")

def main():
    trig(6)
main()
