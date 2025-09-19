import customtkinter as ctk
import utility as util
import colors
import json

class AskQuestionsFrame:
    def __init__(self, main_frame, selected_topics: list):
        self.main_frame = main_frame
        self.selected_topics = selected_topics
        self.question = self.get_question()
        
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=0)

        self.question_label = ctk.CTkLabel(main_frame, text=self.question, text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR), font=("Calibre", 24))
        self.question_label.grid(row=0, column=0, padx=20, pady=20)

    def get_question(self):
        return "question"

        