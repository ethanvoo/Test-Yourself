import customtkinter as ctk
import utility as utils
import colors

class WordFrame(ctk.CTkFrame):
    def __init__(self, master, subject_add_to, topic):
        super().__init__(master)

        self.answer = ctk.StringVar()
        self.current_row = 0
        self.answer_buttons: list = []
        self.awarded_words: list[str] = []

        self.subject_add_to = subject_add_to
        self.topic = topic

        self.grid(column=0, row=3, columnspan=3, padx=20, pady=20, sticky="nesw")
        self.columnconfigure((0, 1), weight=1)
        

        self.add_question_label = ctk.CTkLabel(self, text='Add Question:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.add_question_label.grid(row=0, column=0, padx=20, pady=20,  sticky="w")

        self.add_question_entry = ctk.CTkEntry(self, width=280, height=28,)
        self.add_question_entry.grid(column=1, row=0, padx=20, pady=20, sticky="w")

        self.add_answer_label = ctk.CTkLabel(self, text='Add Answer:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.add_answer_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.add_answer_entry = ctk.CTkEntry(self, textvariable=self.answer, width=280, height=28,)
        self.answer.trace_add("write", self.input_callback)

        self.add_answer_entry.grid(column=1, row=1, padx=20, pady=20, sticky="w")

        self.answer_marks_frame = ctk.CTkScrollableFrame(self, fg_color='transparent')
        self.answer_marks_frame.grid(row=2, column=0, padx=20,columnspan=2, sticky="ew")

        self.add_question_button = ctk.CTkButton(self, text="Add Question", height=40, command=self.create_question)
        self.add_question_button.grid(column=0, padx=20, pady=20, row=3, columnspan=2, sticky="ew")
    
    def input_callback(self, var, index, mode):

        current_input: str = self.answer.get()
        self.answer_word_list: list[str] = [word.strip() for word in current_input.split(' ') if word != '']
        
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
    
    def add_question_to_file(self, subject: str, topic: str, question: str, answer: str, awarded_words):
        if subject == '<None>' or topic == '<None>' or question == '' or answer == '':
            self.error_label = ctk.CTkLabel(self, text="Please fill in all fields", fg_color='transparent', font=("Calibre", 23), text_color=utils.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.error_label.grid(row=5, column=0, padx=20, pady=20, columnspan=2)
            return
        

        data: dict = utils.get_choice(subject, "r")
        if "error" in data:
            self.error_label = ctk.CTkLabel(self, text=data["error"], fg_color='transparent', font=("Calibre", 23), text_color=utils.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.error_label.grid(row=4, column=0, padx=20, pady=20, columnspan=2)
            return
        
        if topic not in data:
            return
        
        data[topic].append({"multiple_choice":False, "question": question,
                            "answer": answer,
                            "awarded_words": awarded_words, "choices":[]})
        
        self.awarded_words = []
        
        utils.get_choice(subject, "w", write_data=data)
        self.add_answer_entry.delete(0, 'end')
        self.add_question_entry.delete(0, 'end')


    def create_question(self):
        awarded_words = utils.remove_punctuation(self.awarded_words)

        question = self.add_question_entry.get()
        answer = self.add_answer_entry.get()

        print(self.subject_add_to, self.topic, question, answer, awarded_words)

        self.add_question_to_file(self.subject_add_to, self.topic, question, answer, awarded_words)