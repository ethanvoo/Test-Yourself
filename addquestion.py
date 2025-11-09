import customtkinter as ctk
import utility as utils
import colors
import choosesubjectframe
import os

class AddQuestionsFrame:
    def __init__(self, master, subject: str):
        self.subject_add_to: str = subject
        self.topic_add_to: str = ""
        self.topics_list: list = []
        self.answer: ctk.StringVar = ctk.StringVar()
        self.answer_buttons: list = []
        self.awarded_words: list[str] = []
        self.master = master

        if not subject in utils.get_subjects():
            utils.add_subject(self.subject_add_to)
        
        self.add_questions_frame = ctk.CTkFrame(master)
        self.add_questions_frame.grid(row=0, column=0, sticky="nesw", columnspan=2)
        self.add_questions_frame.grid_rowconfigure(0, weight=0)
        self.add_questions_frame.grid_rowconfigure(4, weight=1)
        self.add_questions_frame.grid_columnconfigure((0, 1), weight=1)

        self.subject_label = ctk.CTkLabel(self.add_questions_frame,
                                                 text=self.subject_add_to,
                                                  width=30,
                                                  height=28,
                                                  fg_color='transparent',
                                                  font=("Calibre", 23))
        self.subject_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        self.choose_topic_label = ctk.CTkLabel(self.add_questions_frame, text='Choose Topic:',
                                        width=30, 
                                        height=28, 
                                        fg_color='transparent', 
                                        font=("Calibre", 23))
        self.choose_topic_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        

        topics = utils.get_choice(self.subject_add_to, "r")
        self.topics_list = list(topics.keys())

        init_option_value: str = self.topics_list[0] if self.topics_list else '<None>'

        self.topic_optionmenu_var = ctk.StringVar(value=init_option_value)
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

        self.answer_marks_frame = ctk.CTkScrollableFrame(self.add_questions_frame, fg_color='transparent')
        self.answer_marks_frame.grid(row=4, column=0, padx=20,columnspan=2, sticky="ew")

        


        self.add_question_button = ctk.CTkButton(self.add_questions_frame, text="Add Question", height=40, command=self.create_question)
        self.add_question_button.grid(column=0, padx=20, pady=20, row=6, columnspan=2, sticky="ew")

        self.go_back_button = ctk.CTkButton(self.master,
                                        text="Go Back",
                                        command=self.go_back_callback)
        self.go_back_button.grid(column=1, sticky="e", padx=10, pady=10)
    
    def go_back_callback(self):
        self.add_questions_frame.destroy()
        self.go_back_button.destroy()
        choose_subject_frame = choosesubjectframe.ChooseSubjectFrame(self.master)
        choose_subject_frame.grid(column=0, row=0, sticky="nesw", padx=20, pady=20, columnspan=3)

    def input_callback(self, var, index, mode):

        current_input: str = self.answer.get()
        self.answer_word_list: list[str] = [word.strip() for word in current_input.split(' ') if word != '']
        print(self.answer_word_list)
        
        for widget in self.answer_marks_frame.winfo_children():
            widget.destroy()
        row = 0
        col = 0
        for word in self.answer_word_list:
            print(row, col, word)
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
                                   border_color=utils.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                   text_color=utils.rgb_to_hex(colors.MAIN_TEXT_COLOR), 
                                   command=lambda args=word: self.button_callback(args))
            button.grid(row=row, column=col)
            
            col += 1
        
        
    def button_callback(self, word):
        for button in self.answer_marks_frame.winfo_children():
            if button.cget("text") == word:
                if button.cget("fg_color") == "transparent":
                    button.configure(fg_color=utils.rgb_to_hex(colors.MAIN_BUTTON_COLOR), text_color=utils.rgb_to_hex(colors.MAIN_TEXT_COLOR)) # type: ignore
                    self.awarded_words.append(word)
                else:
                    button.configure(fg_color="transparent", text_color=utils.rgb_to_hex(colors.MAIN_TEXT_COLOR)) # type: ignore
                    self.awarded_words.remove(word)
                break
            

    def add_topic_callback(self):
        message = ctk.CTkInputDialog(text="Enter Topic Name:", title="Add Topic")
        topic_name = message.get_input()
        
        data: dict = utils.get_choice(self.subject_add_to, "r")
        data[topic_name] = []
        
        utils.get_choice(self.subject_add_to, "w", write_data=data)

        topics = utils.get_choice(self.subject_add_to, "r")
        self.topics_list = list(topics.keys())

        self.topic_optionmenu_var = ctk.StringVar(value='<None>')
        self.topic_optionmenu = ctk.CTkOptionMenu(self.add_questions_frame, values=self.topics_list,
                                                width=140, height=28,
                                                command=self.topic_optionmenu_callback,
                                                variable=self.topic_optionmenu_var)
        self.topic_optionmenu.grid(column=1, row=1, padx=20, pady=20, sticky="w")
    
    def topic_optionmenu_callback(self, value):
        self.topic_add_to = value


    def add_question_to_file(self, subject: str, topic: str, question: str, answer: str, awarded_words):
        if subject == '<None>' or topic == '<None>' or question == '' or answer == '':
            self.error_label = ctk.CTkLabel(self.add_questions_frame, text="Please fill in all fields", fg_color='transparent', font=("Calibre", 23), text_color=utils.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.error_label.grid(row=5, column=0, padx=20, pady=20, columnspan=2)
            return
        

        data: dict = utils.get_choice(subject, "r")
        if "error" in data:
            self.error_label = ctk.CTkLabel(self.add_questions_frame, text=data["error"], fg_color='transparent', font=("Calibre", 23), text_color=utils.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.error_label.grid(row=4, column=0, padx=20, pady=20, columnspan=2)
            return
        
        if topic not in data:
            return
        
        data[topic].append({"question": question,
                            "answer": answer,
                            "awarded_words": awarded_words})
        
        self.awarded_words = []
        
        utils.get_choice(subject, "w", write_data=data)
        self.add_answer_entry.delete(0, 'end')
        self.add_question_entry.delete(0, 'end')


    def create_question(self):
        awarded_words = utils.remove_punctuation(self.awarded_words)
        displayed_widgets = self.add_questions_frame.winfo_children()

        answer: str = ''
        question: str = ''
        topic: str = ''
        for i, displayed_widget in enumerate(displayed_widgets):
            if displayed_widget.winfo_name() == "!ctkentry":
                question = displayed_widget.get()
            elif displayed_widget.winfo_name() == "!ctkentry2":
                answer = displayed_widget.get()
            elif displayed_widget.winfo_name() == "!ctkoptionmenu":
                topic = self.topic_optionmenu_var.get()

        self.add_question_to_file(self.subject_add_to, topic, question, answer, awarded_words)