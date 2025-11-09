import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import addquestion


import utility as utils


class ChooseSubjectFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.subjects: list = utils.get_subjects()
        self.matched_topics: list = []
        self.button_list: list = []

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((3), weight=1)

        self.title = ctk.CTkLabel(self, text="Choose a subject", font=("Calibre", 30))
        self.title.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.search_bar_var = ctk.StringVar()

        self.search_bar = ctk.CTkEntry(self, textvariable=self.search_bar_var)
        self.search_bar.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5)
        self.search_bar_var.trace_add("write", self.search_bar_callback)

        self.add_subject_button = ctk.CTkButton(self, text="Add Subject", command=self.add_subject_button_callback)
        self.add_subject_button.grid(row=2, column=2, sticky="ew", padx=5)

        self.display_subject_scrollableframe = ctk.CTkScrollableFrame(self)
        self.display_subject_scrollableframe.grid(row=3, column=0, columnspan=3, sticky="nesw")
        if self.subjects:
            self.display_subject_scrollableframe.grid_rowconfigure([i for i in range(len(self.subjects))], weight=1)
        else:
            self.display_subject_scrollableframe.grid_rowconfigure(0, weight=1)
        self.display_subject_scrollableframe.grid_columnconfigure((0, 1), weight=1)

        self.search_bar_callback()

        self.go_back_button = ctk.CTkButton(self.master,
                                        text="Go Back",
                                        command=self.go_back_button_callback)
        self.go_back_button.grid(column=2,row=1, sticky="e", padx=10, pady=10)
    
    def go_back_button_callback(self):
        from start_frame import StartFrame
        self.destroy()
        self.go_back_button.destroy()
        self.start_frame = StartFrame(self.master)
        self.start_frame.grid(row=0, column=0, columnspan=2, sticky="nesw", rowspan=3)
    
    
    
    def search_bar_callback(self, *args):
        search_bar_value = self.search_bar_var.get()
        length = len(search_bar_value)
        self.matched_topics = [s for s in self.subjects if search_bar_value.lower() in s[0:length].lower()]

        for widget in self.display_subject_scrollableframe.winfo_children():
            widget.destroy()  # deleting widget
            self.button_list = []


        for i, subject in enumerate(self.matched_topics):
            
            button = ctk.CTkButton(self.display_subject_scrollableframe, text=subject, fg_color='transparent', border_width=1, height=60, command=lambda s=subject: self.button_callback(s))
            
            button.grid(row=i, column=0, columnspan=2, sticky="ew", pady=10)

            self.button_list.append(button)
        
    def button_callback(self, subject):
        self.destroy_elements()
        addquestion.AddQuestionsFrame(self.master, subject)
    
    def destroy_elements(self):
        self.destroy()
        self.go_back_button.destroy()

    def add_subject_button_callback(self):
        search_bar_value = self.search_bar_var.get()

        if not search_bar_value:
            CTkMessagebox(title="Error", message="The subject must have a name!", icon="warning")
            return

        if search_bar_value.lower() in utils.get_subjects():
            CTkMessagebox(title="Error", message="This topic already exists!", icon="warning")
            return
        
        self.destroy_elements() 
        addquestion.AddQuestionsFrame(self.master, search_bar_value)


        






