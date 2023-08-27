import random
from os import system
from time import sleep
from fractions import Fraction
from math import sin, cos, tan, pi

class TrigPro:
    def __init__(self, problems):
        self.functions = {"sin": sin, "tan": tan, "cos": cos}

        self.angles = {"π/6": pi/6, "π/4": pi/4, "π/3": pi/3, "π/2": pi/2,
                       "2π/3": (2*pi)/3, "3π/4": (3*pi)/4, "5π/6": (5*pi)/6,
                       "π": pi, "7π/6": (7*pi)/6, "5π/4": (5*pi)/4,
                       "4π/3": (4*pi/3), "3π/2": (3*pi)/2, "5π/3": (5*pi)/3,
                       "7π/4": (7*pi)/4, "11π/6": (11*pi)/6,
                       "2π": 2*pi, "0π": 0*pi}
        
        self.answers = {
            Fraction(7836263351624663, 9007199254740992): "√3/2",
            Fraction(-7836263351624663, 9007199254740992): "-√3/2",
            Fraction(7836263351624663, 9007199254740992): "√3/2", 
            Fraction(-7836263351624663,9007199254740992): "-√3/2",
            Fraction(-799388933858263,1125899906842624): "-√2/2", 
            Fraction(799388933858263,1125899906842624): "√2/2",
            Fraction(-5224175567749775,9007199254740992): "-√3/3", 5224175567749775/9007199254740992: "√3/3",
            Fraction(-3895613677675479,2251799813685248): "-√3", 3895613677675479/2251799813685248: "√3",
            Fraction(5443746451065123, 1): "undefined", 
            Fraction(16331239353195370, 1): "undefined"
        }

        self.problems = problems
        self.correct = 0
        self.wrong = 0
        self.current_streak = 0
        self.max_streak = 0

    def generate_problem(self):
        randnom_angle = random.choice(list(self.angles.keys()))
        random_function = random.choice(list(self.functions.keys()))
        return randnom_angle, random_function

    def check_answer(self, user_answer, problem):
        randnom_angle, random_function = problem
        answer = self.calculate_answer(random_function, randnom_angle)

        if user_answer == answer:
            self.correct += 1
            self.current_streak += 1
            if self.current_streak > self.max_streak:
                self.max_streak = self.current_streak
            return True
        else:
            self.current_streak = 0
            self.wrong += 1
            return False

    def calculate_answer(self, function_name, angle_name):
        angle = self.angles[angle_name]
        function = self.functions[function_name]
        result = Fraction(round(function(angle), 2))

        if result in self.answers:
            return self.answers[result]
        else:
            return str(result)

    def run_quiz(self):
        for i in range(self.problems):
            system("clear")
            problem = self.generate_problem()
            user_answer = input(f"\nWhat is the value of {problem[1]}({problem[0]})?")

            while not self.validate_answer(user_answer):
                user_answer = input("Invalid answer. Try again: ")

            result = self.check_answer(user_answer, problem)

            system("clear")
            if result:
                self.display_correct_feedback()
            else:
                self.display_wrong_feedback(problem)

    def validate_answer(self, answer):
        # Add validation logic here (e.g., check if answer is numeric or within a valid range)
        return True  # For simplicity, always return True for now

    def display_correct_feedback(self):
        sleep(1)
        print("\n✅ Correct!")
        if self.current_streak > 2:
            print(f"🔥 {self.current_streak}")
        sleep(0.5)
        input("\nENTER to continue...")

    def display_wrong_feedback(self, problem):
        if self.current_streak > 2:
            print("🔥 0")
        sleep(1)
        print(f"\n❌ The answer is: {problem[1]}({problem[0]})")
        sleep(0.5)
        input("\nENTER to continue.")

    def display_results(self):
        system("clear")
        print(f"\n🔥 {self.max_streak} | ✅ {self.correct} | ❌ {self.wrong}\n")

def main():
    quiz = TrigPro(6)
    quiz.run_quiz()
    quiz.display_results()

if __name__ == "__main__":
    main()
