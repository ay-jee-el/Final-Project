import tkinter as tk
from quiz_questions import quiz_qna

class Quiz:
    def __init__(self, question = 0, score = 0):
        # boots up quiz? 

        self.question = question
        self.score = score
        self.questions = quiz_qna

    # questions, answer, choiches, LAYOUT for all this, calucations for correct nd wrong, output
    # ^^ will include aspects of the quiz. likle ywilll need various defs
        def layout(self):
            #layout and imports for tkinter layout (look into this)
            self.lable =

        def check_answer(self):
            # if check if the "choice" olines up with what was clicked
            # if answer == "answer", then score += 1 (?)

        def next(self):
            #moves on the next question

        def calculate(self):
            # math for how many correct



if __name__ == "__main__":
    # Seems like tkinter operates differently than traditional pygames main? Using notes and info about tkinter for this part
    # Dont mess w for now
    root = tk.Tk()
    quiz = Quiz(root)
    root.mainloop