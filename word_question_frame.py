<<<<<<< HEAD
import customtkinter as ctk
import utility as util
import colors

class WordQuestionFrame(ctk.CTkFrame):
    def __init__(self, master, answer: str):
        super().__init__(master)

        self.answer = answer

        
        self.enter_answer_var = ctk.StringVar()
        self.enter_answer_entry = ctk.CTkEntry(self, textvariable=self.enter_answer_var, placeholder_text="Answer", font=("Calibre", 24))
        self.enter_answer_entry.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

    def get_answer(self):
=======
import customtkinter as ctk
import utility as util
import colors

class WordQuestionFrame(ctk.CTkFrame):
    def __init__(self, master, answer: str):
        super().__init__(master)

        self.answer = answer

        
        self.enter_answer_var = ctk.StringVar()
        self.enter_answer_entry = ctk.CTkEntry(self, textvariable=self.enter_answer_var, placeholder_text="Answer", font=("Calibre", 24))
        self.enter_answer_entry.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

    def get_answer(self):
>>>>>>> 517dea2480b3a0eb13dac1b4bb20b7edf32e9b15
        return self.enter_answer_var.get()