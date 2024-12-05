import tkinter as tk
from tkinter import messagebox
from quiz_questions import quiz_qna

class Quiz:
    def __init__(self, master):
        # boots up quiz? 
        self.master = master
        self.qn = 0
        self.score = 0
        self.questions = quiz_qna

        self.layout()

    def layout(self):
        root.geometry("600x250")
        root.configure(bg="lightblue")
        self.label = tk.Label(self.master, text=self.questions[self.qn]["question"], fg="darkblue", bg="lightblue", font=("Helvetica", 14))
        self.label.pack(pady=10)
        self.next_button = tk.Button(self.master, text="Next", command=self.check_answer, bg="darkblue", fg="lightblue", font=("Helvetica", 14))
        self.next_button.pack(pady=10)

        self.var = tk.StringVar()

        for option in self.questions[self.qn]["options"]:
            rb = tk.Radiobutton(self.master, text=option, variable=self.var, value=option, fg="darkblue", bg="lightblue", font=("Helvetica", 12))
            rb.pack()


    def check_answer(self):
            if self.var.get() == self.questions[self.qn]["answer"]:
                self.score += 1

            self.qn += 1

            if self.qn < len(self.questions):
                 self.next()
            else:
                 self.calculate()

    def next(self):
            self.label.config(text=self.questions[self.qn]["question"])
            for wgt in self.master.winfo_children():
                 if isinstance(wgt, tk.Radiobutton):
                      wgt.destroy()
            
            for option in self.questions[self.qn]["options"]:
                 radiobutton = tk.Radiobutton(self.master, text=option, variable=self.var, value=option, fg="darkblue", bg="lightblue", font=("Helvetica", 12))
                 radiobutton.pack()

    def calculate(self):
        messagebox.showinfo("Complete!",f"Your score: {self.score}/{len(self.questions)}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    quiz = Quiz(root)
    root.mainloop()