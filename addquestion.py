import customtkinter as ctk
import utility as utils
import choosesubjectframe
from  multiple_choice_frame import MultipleChoiceFrame
from  word_frame import WordFrame

class AddQuestionsFrame(ctk.CTkFrame):
    def __init__(self, master, subject: str):
        super().__init__(master)
        self.subject_add_to: str = subject
        self.topic_add_to: str = ""
        self.topics_list: list = []
        self.master = master
        

        if subject not in utils.get_subjects():
            utils.add_subject(self.subject_add_to)
        
        self.grid(row=0, column=0, sticky="nesw", columnspan=2)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.subject_label = ctk.CTkLabel(self,
                                                 text=self.subject_add_to,
                                                  width=30,
                                                  height=28,
                                                  fg_color='transparent',
                                                  font=("Calibre", 23))
        self.subject_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        self.choose_topic_label = ctk.CTkLabel(self, text='Choose Topic:',
                                        width=30, 
                                        height=28, 
                                        fg_color='transparent', 
                                        font=("Calibre", 23))
        self.choose_topic_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        

        topics = utils.get_choice(self.subject_add_to, "r")
        self.topics_list = list(topics.keys())

        init_option_value: str = self.topics_list[0] if self.topics_list else '<None>'

        self.topic_optionmenu_var = ctk.StringVar(value=init_option_value)
        self.topic_optionmenu = ctk.CTkOptionMenu(self, values=self.topics_list, width=140, height=28, command=self.topic_optionmenu_callback, variable=self.topic_optionmenu_var)
                                                
        self.topic_optionmenu.grid(column=1, row=1, padx=20, pady=20, sticky="w")

        self.add_topic_button = ctk.CTkButton(self,
                                        text="Add", 
                                        width=10, 
                                        command=self.add_topic_callback)
        self.add_topic_button.grid(column=1, padx=20, pady=20, row=1, sticky="e")

        self.question_type_label = ctk.CTkLabel(self, text="Question Type", width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.question_type_label.grid(row=2, column = 0, padx=20, pady=20,  sticky="w")
        
        self.question_type_frame = ctk.CTkFrame(self)
        self.question_type_frame.grid(row=2, column=1, columnspan=2)

        self.radio_var = ctk.StringVar(value="word")

        self.word_question_radio = ctk.CTkRadioButton(self.question_type_frame, text="Word Question", command=self.word_question_radio_callback, variable=self.radio_var, value="word")
        self.word_question_radio.grid(column=0, row=0, padx=20)

        self.mc_question_radio = ctk.CTkRadioButton(self.question_type_frame, text="Multiple Choice", command=self.mc_question_radio_callback, variable=self.radio_var, value="mc")
        self.mc_question_radio.grid(column=1, row=0, padx=20)

        

        

        self.go_back_button = ctk.CTkButton(self.master,
                                        text="Go Back",
                                        command=self.go_back_callback)
        self.go_back_button.grid(column=1, sticky="e", padx=10, pady=10)
    
    def word_question_radio_callback(self):
        try:
            self.multiple_choice_frame.destroy()

        except Exception as e:
            print("Unable to delete frame Possibly no longer exists!", e)
        self.word_frame = WordFrame(self, subject_add_to=self.subject_add_to, topic=self.topic_optionmenu_var.get())
        self.word_frame.grid(column=0, row=3, columnspan=3, padx=20, pady=20, sticky="nesw")
        
        
        
    

    def mc_question_radio_callback(self):
        try:
            self.word_frame.destroy()
        except Exception as e:
            print("Unable to delete frame Possibly no longer exists!", e)
        self.multiple_choice_frame = MultipleChoiceFrame(self, self.subject_add_to, self.topic_optionmenu_var.get())
        self.multiple_choice_frame.grid(column=0, row=3, columnspan=3, padx=20, pady=20, sticky="nesw")


    
    def remove_elements(self, frame):
        print("removing from", frame)
        try:
            elems = frame.winfo_children()
            for elem in elems:
                elem.destroy()
            
        except Exception as e:
            print(e)
        
    
    
    def add_answer_button_callback(self):
        if self.answer == "":
            return
        
        self.checkbox = ctk.CTkCheckBox(self.multiple_choices_frame)
        self.checkbox.grid(row=self.current_row, column=0, padx=10, pady=10)

        self.choice_answer_label = ctk.CTkLabel(self.multiple_choices_frame, text=self.answer)
        self.choice_answer_label.grid(row=self.current_row, column=1, padx=10, pady=10)

        self.current_row += 1
        self.answer.set("")
    
    
    
    
    def go_back_callback(self):
        self.destroy()
        self.go_back_button.destroy()
        choose_subject_frame = choosesubjectframe.ChooseSubjectFrame(self.master)
        choose_subject_frame.grid(column=0, row=0, sticky="nesw", padx=20, pady=20, columnspan=3)

            

    def add_topic_callback(self):
        message = ctk.CTkInputDialog(text="Enter Topic Name:", title="Add Topic")
        topic_name = message.get_input()
        
        data: dict = utils.get_choice(self.subject_add_to, "r")
        data[topic_name] = []
        
        utils.get_choice(self.subject_add_to, "w", write_data=data)

        topics = utils.get_choice(self.subject_add_to, "r")
        self.topics_list = list(topics.keys())

        self.topic_optionmenu_var = ctk.StringVar(value='<None>')
        self.topic_optionmenu = ctk.CTkOptionMenu(self, values=self.topics_list,
                                                width=140, height=28,
                                                command=self.topic_optionmenu_callback,
                                                variable=self.topic_optionmenu_var)
        self.topic_optionmenu.grid(column=1, row=1, padx=20, pady=20, sticky="w")
    
    def topic_optionmenu_callback(self, value):
        self.topic_add_to = value


    