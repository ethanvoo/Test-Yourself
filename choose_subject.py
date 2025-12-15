<<<<<<< HEAD
import customtkinter as ctk
import utility as util

class ChooseSubjectListFrame():
    def __init__(self, main_frame, remake_frame):
        self.main_frame = main_frame
        self.remake_frame = remake_frame
        self.subjects: list[str] = util.get_subjects()

        self.main_frame.columnconfigure((0, 1), 1)

        self.title_label = ctk.CTkLabel(main_frame, text="Choose Subject to add a question to.")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        for i, subject in enumerate(self.subjects):
            subject_frame = ctk.CTkFrame(main_frame)
            subject_frame.grid(row=i, column=0, columnspan=2, sticky="ew", border_width=5)

            subject_label = ctk.CTkLabel(subject_frame, text=subject)
            subject_label.grid(row=0, column=0, padx=10, pady=10)
=======
import customtkinter as ctk
import utility as util

class ChooseSubjectListFrame():
    def __init__(self, main_frame, remake_frame):
        self.main_frame = main_frame
        self.remake_frame = remake_frame
        self.subjects: list[str] = util.get_subjects()

        self.main_frame.columnconfigure((0, 1), 1)

        self.title_label = ctk.CTkLabel(main_frame, text="Choose Subject to add a question to.")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        for i, subject in enumerate(self.subjects):
            subject_frame = ctk.CTkFrame(main_frame)
            subject_frame.grid(row=i, column=0, columnspan=2, sticky="ew", border_width=5)

            subject_label = ctk.CTkLabel(subject_frame, text=subject)
            subject_label.grid(row=0, column=0, padx=10, pady=10)
>>>>>>> 517dea2480b3a0eb13dac1b4bb20b7edf32e9b15
