<<<<<<< HEAD
import customtkinter as ctk
import utility as utils

class MultipleChoiceFrame(ctk.CTkFrame):
    def __init__(self, master, subject: str, topic: str):
        super().__init__(master)

        self.row: int = 0
        self.choices: list = []
        self.subject = subject
        self.topic = topic

        self.answer = ctk.StringVar()

        self.grid(column=0, row=3, columnspan=3, padx=20, pady=20, sticky="nesw")
        self.columnconfigure((0, 1), weight=1)

        self.add_question_label = ctk.CTkLabel(self, text='Add Question:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.add_question_label.grid(row=0, column=0, padx=20, pady=20,  sticky="w")

        self.add_question_entry = ctk.CTkEntry(self, width=280, height=28)
        self.add_question_entry.grid(column=1, row=0, padx=20, pady=20, sticky="w")

        self.add_answer_label = ctk.CTkLabel(self, text='Add Answer:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.add_answer_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.add_answer_entry = ctk.CTkEntry(self, textvariable=self.answer, width=280, height=28,)
        self.add_answer_entry.grid(column=1, row=1, padx=20, pady=20, sticky="w")

        self.add_answer_button = ctk.CTkButton(self, text="Add", command=self.add_choice_callback)
        self.add_answer_button.grid(column=2, row=1)

        self.choices_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.choices_frame.grid(row=2, column=0, padx=20,columnspan=3, sticky="ew")

        self.add_question_button = ctk.CTkButton(self, text="Add Question", height=40, command=self.create_question)
        self.add_question_button.grid(column=0, padx=20, pady=20, row=3, columnspan=2, sticky="ew")
    
    def add_choice_callback(self):
        if self.add_answer_entry.get() == "":
            return
            #do error label stiff
        
        if self.row > 4:
            return
            # do some error stuff
        
        if self.add_answer_entry.get() in self.choices:
            return
            #error stuff
        
            self.add_answer_entry.delete(0, 'end')

        
        self.choices.append(self.add_answer_entry.get())
        
        checkbox = ctk.CTkCheckBox(self.choices_frame, text=self.add_answer_entry.get())
        checkbox.grid(padx=10, pady=10, row=self.row)

        self.row +=1
        

    
    def create_question(self):
        checkboxes: list = self.choices_frame.winfo_children()
        checkbox_values: list = [values.get() for values in checkboxes]
        if 1 not in checkbox_values:
            return
            

        self.column = 0

        question: str  = self.add_question_entry.get()
        for i, checkbox in enumerate(checkboxes):
            if checkbox_values[i] == 1:
                answer = checkbox.cget("text")
        
        topic = self.topic
        subject = self.subject

        

        data: dict = utils.get_choice(subject, "r")

        if "error" in data:
            print("error in data")
            # self.error_label = ctk.CTkLabel(self, text=data["error"], fg_color='transparent', font=("Calibre", 23), text_color=utils.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            # self.error_label.grid(row=4, column=0, padx=20, pady=20, columnspan=2)
            
            return
        
        if topic not in data:
            print("topic not in data")
            return
        checkboxes = self.choices_frame.winfo_children()
        data[topic].append({"multiple_choice":True, "question": question,
                            "answer": answer,
                            "awarded_words": [],
                            "choices":[checkbox.cget("text") for checkbox in checkboxes]})
    
        utils.get_choice(subject, "w", write_data=data)
        self.add_answer_entry.delete(0, 'end')
        self.add_question_entry.delete(0, 'end')
        
        for checkbox in checkboxes:
            checkbox.destroy()


=======
import customtkinter as ctk
import utility as utils

class MultipleChoiceFrame(ctk.CTkFrame):
    def __init__(self, master, subject: str, topic: str):
        super().__init__(master)

        self.row: int = 0
        self.choices: list = []
        self.subject = subject
        self.topic = topic

        self.answer = ctk.StringVar()

        self.grid(column=0, row=3, columnspan=3, padx=20, pady=20, sticky="nesw")
        self.columnconfigure((0, 1), weight=1)

        self.add_question_label = ctk.CTkLabel(self, text='Add Question:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.add_question_label.grid(row=0, column=0, padx=20, pady=20,  sticky="w")

        self.add_question_entry = ctk.CTkEntry(self, width=280, height=28)
        self.add_question_entry.grid(column=1, row=0, padx=20, pady=20, sticky="w")

        self.add_answer_label = ctk.CTkLabel(self, text='Add Answer:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.add_answer_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.add_answer_entry = ctk.CTkEntry(self, textvariable=self.answer, width=280, height=28,)
        self.add_answer_entry.grid(column=1, row=1, padx=20, pady=20, sticky="w")

        self.add_answer_button = ctk.CTkButton(self, text="Add", command=self.add_choice_callback)
        self.add_answer_button.grid(column=2, row=1)

        self.choices_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.choices_frame.grid(row=2, column=0, padx=20,columnspan=3, sticky="ew")

        self.add_question_button = ctk.CTkButton(self, text="Add Question", height=40, command=self.create_question)
        self.add_question_button.grid(column=0, padx=20, pady=20, row=3, columnspan=2, sticky="ew")
    
    def add_choice_callback(self):
        if self.add_answer_entry.get() == "":
            return
            #do error label stiff
        
        if self.row > 4:
            return
            # do some error stuff
        
        if self.add_answer_entry.get() in self.choices:
            return
            #error stuff
        
            self.add_answer_entry.delete(0, 'end')

        
        self.choices.append(self.add_answer_entry.get())
        
        checkbox = ctk.CTkCheckBox(self.choices_frame, text=self.add_answer_entry.get())
        checkbox.grid(padx=10, pady=10, row=self.row)

        self.row +=1
        

    
    def create_question(self):
        checkboxes: list = self.choices_frame.winfo_children()
        checkbox_values: list = [values.get() for values in checkboxes]
        if 1 not in checkbox_values:
            return
            

        self.column = 0

        question: str  = self.add_question_entry.get()
        for i, checkbox in enumerate(checkboxes):
            if checkbox_values[i] == 1:
                answer = checkbox.cget("text")
        
        topic = self.topic
        subject = self.subject

        

        data: dict = utils.get_choice(subject, "r")

        if "error" in data:
            print("error in data")
            # self.error_label = ctk.CTkLabel(self, text=data["error"], fg_color='transparent', font=("Calibre", 23), text_color=utils.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            # self.error_label.grid(row=4, column=0, padx=20, pady=20, columnspan=2)
            
            return
        
        if topic not in data:
            print("topic not in data")
            return
        checkboxes = self.choices_frame.winfo_children()
        data[topic].append({"multiple_choice":True, "question": question,
                            "answer": answer,
                            "awarded_words": [],
                            "choices":[checkbox.cget("text") for checkbox in checkboxes]})
    
        utils.get_choice(subject, "w", write_data=data)
        self.add_answer_entry.delete(0, 'end')
        self.add_question_entry.delete(0, 'end')
        
        for checkbox in checkboxes:
            checkbox.destroy()


>>>>>>> 517dea2480b3a0eb13dac1b4bb20b7edf32e9b15
        