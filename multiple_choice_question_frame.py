<<<<<<< HEAD
import customtkinter as ctk
import utility as util
import colors

class MultipleChoiceQuestionFrame(ctk.CTkFrame):
    def __init__(self, master, choices: list):
        super().__init__(master)

        self.choices: list = choices

        for i, choice in enumerate(choices):
            checkbox = ctk.CTkCheckBox(self, text=choice)
            checkbox.grid(row=i, column=0, padx=20, pady=20)

    def get_answer(self) -> str | None:
        checkboxes = self.winfo_children()
        checkbox_ticked_amount: int = 0
        for i, checkbox in enumerate(checkboxes):
            if checkbox.get() == 1:
                answer = checkbox.cget("text")
                checkbox_ticked_amount += 1
        
        if checkbox_ticked_amount > 1:
            return None
        return answer

=======
import customtkinter as ctk
import utility as util
import colors

class MultipleChoiceQuestionFrame(ctk.CTkFrame):
    def __init__(self, master, choices: list):
        super().__init__(master)

        self.choices: list = choices

        for i, choice in enumerate(choices):
            checkbox = ctk.CTkCheckBox(self, text=choice)
            checkbox.grid(row=i, column=0, padx=20, pady=20)

    def get_answer(self) -> str | None:
        checkboxes = self.winfo_children()
        checkbox_ticked_amount: int = 0
        for i, checkbox in enumerate(checkboxes):
            if checkbox.get() == 1:
                answer = checkbox.cget("text")
                checkbox_ticked_amount += 1
        
        if checkbox_ticked_amount > 1:
            return None
        return answer

>>>>>>> 517dea2480b3a0eb13dac1b4bb20b7edf32e9b15
        