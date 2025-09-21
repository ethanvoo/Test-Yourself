import customtkinter as ctk
import utility as util
import colors

class AddQuestionsFrame:
    def __init__(self, master):
        self.subject_add_to: str = ""
        self.topic_add_to: str = ""
        self.topics_list: list = []
        self.answer: ctk.StringVar = ctk.StringVar()
        self.awarded_words: list = []

        self.add_questions_frame = ctk.CTkFrame(master)
        self.add_questions_frame.grid(row=0, column=0, sticky="nesw", padx=20, pady=20)
        self.add_questions_frame.grid_rowconfigure(0, weight=0)
        self.add_questions_frame.grid_rowconfigure(4, weight=1)
        self.add_questions_frame.grid_columnconfigure((0, 1), weight=1)

        self.choose_subject_label = ctk.CTkLabel(self.add_questions_frame,
                                                 text='Choose Subject:',
                                                  width=30,
                                                  height=28,
                                                  fg_color='transparent',
                                                  font=("Calibre", 23))
        self.choose_subject_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.subject_optionmenu_var = ctk.StringVar(value='<None>')
        self.subject_optionmenu = ctk.CTkOptionMenu(self.add_questions_frame, 
                                                values=['Chemistry', 'Computer Science', "Music"],
                                                width=140, height=28,
                                                command=self.subject_optionmenu_callback,
                                                variable=self.subject_optionmenu_var)
        self.subject_optionmenu.grid(column=1, row=0, padx=20, pady=20, sticky="w")
    
    def subject_optionmenu_callback(self, value):
        self.subject_add_to = value
        self.topic_add_to = ''
        self.choose_topic_label = ctk.CTkLabel(self.add_questions_frame, text='Choose Topic:',
                                        width=30, 
                                        height=28, 
                                        fg_color='transparent', 
                                        font=("Calibre", 23))
        self.choose_topic_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        topics = util.get_choice(value, "r")
        self.topics_list = list(topics.keys())

        self.topic_optionmenu_var = ctk.StringVar(value='<None>')
        self.topic_optionmenu = ctk.CTkOptionMenu(self.add_questions_frame, values=self.topics_list, width=140, height=28, command=self.topic_optionmenu_callback, variable=self.topic_optionmenu_var)
                                                
        self.topic_optionmenu.grid(column=1, row=1, padx=20, pady=20, sticky="w")

        self.add_topic_button = ctk.CTkButton(self.add_questions_frame,
                                        text="Add", 
                                        width=10, 
                                        command=self.add_topic_callback)
        self.add_topic_button.grid(column=1, padx=20, pady=20, row=1, sticky="e")
        
        self.add_question_label = ctk.CTkLabel(self.add_questions_frame, text='Add Question:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.add_question_label.grid(row=2, column=0, padx=20, pady=20,  sticky="w")

        self.add_question_entry = ctk.CTkEntry(self.add_questions_frame, width=280, height=28, placeholder_text='Question')
        self.add_question_entry.grid(column=1, row=2, padx=20, pady=20, sticky="w")

        self.add_answer_label = ctk.CTkLabel(self.add_questions_frame, text='Add Answer:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.add_answer_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")

        self.add_answer_entry = ctk.CTkEntry(self.add_questions_frame, textvariable=self.answer, width=280, height=28, placeholder_text='Answer')
        self.answer.trace_add("write", self.input_callback)

        self.add_answer_entry.grid(column=1, row=3, padx=20, pady=20, sticky="w")

        self.answer_marks_frame = ctk.CTkFrame(self.add_questions_frame, fg_color='transparent')
        self.answer_marks_frame.grid(row=4, column=0, padx=20,columnspan=2)

        


        self.add_question_button = ctk.CTkButton(self.add_questions_frame, text="Add Question", height=40, command=self.create_question)
        self.add_question_button.grid(column=0, padx=20, pady=20, row=5, columnspan=2, sticky="ew")

    def input_callback(self, var, index, mode):
        current_input: str = self.answer.get()
        self.answer_word_list = current_input.split(' ')
        
        for widget in self.answer_marks_frame.winfo_children():
            widget.destroy()
        row = 0
        col = 0
        for word in self.answer_word_list:
            if word == '':
                break
            if col % 5 == 0 and col != 0:
                row += 1
                col = 0
            button = ctk.CTkButton(self.answer_marks_frame, 
                                   text=word, 
                                   width=80, 
                                   fg_color="transparent", 
                                   border_width=1, 
                                   border_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                   text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR), 
                                   command=lambda args=word: self.button_callback(args))
            button.grid(row=row, column=col)
            col += 1

    def button_callback(self, word):
        self.awarded_words.append(word)

    def add_topic_callback(self):
        self.message = ctk.CTkInputDialog(text="Enter Topic Name:", title="Add Topic")
        topic_name = self.message.get_input()
        
        data: dict = util.get_choice(self.subject_add_to, "r")
        data[topic_name] = []
        
        util.get_choice(self.subject_add_to, "w", write_data=data)

        topics = util.get_choice(self.subject_add_to, "r")
        self.topics_list = list(topics.keys())

        self.topic_optionmenu_var = ctk.StringVar(value='<None>')
        self.topic_optionmenu = ctk.CTkOptionMenu(self.add_questions_frame, values=self.topics_list,
                                                width=140, height=28,
                                                command=self.topic_optionmenu_callback,
                                                variable=self.topic_optionmenu_var)
        self.topic_optionmenu.grid(column=1, row=1, padx=20, pady=20, sticky="w")
    
    def topic_optionmenu_callback(self, value):
        self.topic_add_to = value


    def add_question_to_file(self, subject: str, topic: str, question: str, answer: str):
        if subject == '<None>' or topic == '<None>' or question == '' or answer == '':
            print(subject, topic, question, answer)
            self.error_label = ctk.CTkLabel(self.add_questions_frame, text="Please fill in all fields", fg_color='transparent', font=("Calibre", 23), text_color=util.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.error_label.grid(row=5, column=0, padx=20, pady=20, columnspan=2)
            return

        data: dict = util.get_choice(subject, "r")
        if "error" in data:
            self.error_label = ctk.CTkLabel(self.add_questions_frame, text=data["error"], fg_color='transparent', font=("Calibre", 23), text_color=util.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.error_label.grid(row=4, column=0, padx=20, pady=20, columnspan=2)
            return
        
        if topic not in data:
            return
        
        data[topic].append({"question": question,
                            "answer": answer,
                            "awarded_words": self.awarded_words})
        util.get_choice(subject, "w", write_data=data)
        self.add_answer_entry.delete(0, 'end')
        self.add_question_entry.delete(0, 'end')


    def create_question(self):
        displayed_widgets = self.add_questions_frame.winfo_children()
        answer: str = ''
        question: str = ''
        subject: str = ''
        topic: str = ''
        for i, displayed_widget in enumerate(displayed_widgets):
            if displayed_widget.winfo_name() == "!ctkentry":
                question = displayed_widget.get()
            elif displayed_widget.winfo_name() == "!ctkentry2":
                answer = displayed_widget.get()
            elif displayed_widget.winfo_name() == "!ctkoptionmenu":
                subject = self.subject_optionmenu_var.get()
            elif displayed_widget.winfo_name() == "!ctkoptionmenu2":
                topic = self.topic_optionmenu_var.get()

        self.add_question_to_file(subject, topic, question, answer)