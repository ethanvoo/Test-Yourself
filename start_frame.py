import customtkinter as ctk
import utility as util
import colors
from choose_quiz import ChooseQuizFrame
from choosesubjectframe import ChooseSubjectFrame


class StartFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.rowconfigure((1, 2), weight=1)
        self.columnconfigure((0, 1), weight=1)
        self.configure(border_width=5)

        self.title = ctk.CTkLabel(self, 
                         text='Test Yourself', 
                         width=30, height=28, 
                         fg_color='transparent', 
                         font=("Calibre", 40),
                            text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

        self.title.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        self.select_subject_button = ctk.CTkButton(self, 
                                            text="Select Subject",
                                            command=self.select_subject, 
                                            font=("Calibre", 23), 
                                            fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                            text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))
    
        self.select_subject_button.grid(column=0, row=1, padx=20, pady=20, sticky="nesw", columnspan=2)

        self.add_questions_button = ctk.CTkButton(self, 
                                            text="Add Questions",
                                            command=self.add_questions, 
                                            font=("Calibre", 23), 
                                            fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                            text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

        self.add_questions_button.grid(column=0, row=2, padx=20, pady=20, sticky="nesw", columnspan=2)
    
    def add_questions(self):
        self.destroy()
        self.choose_subject_frame = ChooseSubjectFrame(self.master)
        self.choose_subject_frame.grid(column=0, row=0, sticky="nesw", padx=20, pady=20, columnspan=3)

    def select_subject(self):
        self.destroy()
        self.choosequiz_frame = ChooseQuizFrame(self.master)
        self.choosequiz_frame.grid(column=0, row=0, sticky="nsew", padx=20, pady=20, columnspan=3)
    
    def remake_frame(self):
        self.destroy()
