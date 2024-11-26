import tkinter as tk
from tkinter import messagebox
from quiz_questions import quiz_qna

class Quiz:
    #Doesnt appear? runs w no errors tho
    def __init__(self, master):
        # boots up quiz? 
        self.master = master
        self.qn = 0
        self.score = 0
        self.questions = quiz_qna

        self.layout()

    # questions, answer, choiches, LAYOUT for all this, calucations for correct nd wrong, output
    # ^^ will include aspects of the quiz. likle ywilll need various defs
    def layout(self):
            #layout and imports for tkinter layout (look into this)
        self.label = tk.Label(self.master, text=self.questions[self.qn]["question"])
        self.label.pack(pady=10)

        self.var = tk.StringVar()

        for option in self.questions[self.qn]["options"]:
            rb = tk.Radiobutton(self.master, text=option, variable=self.var, value=option)
            rb.pack()

        self.next = tk.Button(self.master, text="Next", command=self.check_answer)
        self.next.pack(pady=10)

    def check_answer(self):
            # if check if the "choice" olines up with what was clicked
            # if answer == "answer", then score += 1 (?)
            if self.var.get() == self.questions[self.qn]["correct"]:
                self.score += 1

            if self.qn < len(self.questions):
                 self.next()
            else:
                 self.calculate()

    def next(self):
            #moves on the next question
            self.label.config(text=self.questions[self.qn]["question"])
            # unsure how this will work; look into it!!
            for wgt in self.master.winfo_children():
                 if isinstance(wgt, tk.Radiobutton):
                      wgt.destroy()
            
            for option in self.questions[self.qn]["options"]:
                 radiobutton = tk.Radiobutton(self.master, text=option, variable=self.var, value=option)
                 radiobutton.pack()

    def calculate(self):
            # math for how many correct
        messagebox.showinfo("Complete")
        self.master.destroy()

if __name__ == "__main__":
    # nsure why if is messing it up?
    # Dont mess w for now
    root = tk.Tk()
    quiz = Quiz(root)
    root.mainloop()