import customtkinter as ctk
import utility as util
import colors
import ask_questions

class ChooseQuizFrame:
    def __init__(self, master, root, back_to_home_btn):
        self.main_frame = master
        self.select_subject_frame = ctk.CTkFrame(master)
        self.selected_topics: list = []
        self.root = root
        self.back_to_home_btn = back_to_home_btn
        self.question_index = 0

        self.select_subject_frame.grid(column=0, row=0, sticky="nsew", padx=20, pady=20)
        self.select_subject_frame.grid_rowconfigure(0, weight=0)
        self.select_subject_frame.grid_columnconfigure((0, 1), weight=1)

        self.label = ctk.CTkLabel(self.select_subject_frame, text='Choose Subject:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.optionmenu_var = ctk.StringVar(value='<None>')
        self.optionmenu = ctk.CTkOptionMenu(self.select_subject_frame, values=['Chemistry', 'Computer Science', "Music"],
                                                width=140, height=28,
                                                command=self.optionmenu_callback,
                                                variable=self.optionmenu_var)
        self.optionmenu.grid(column=1, row=0, padx=20, pady=20)
    
    def optionmenu_callback(self, choice):
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        topics = util.get_choice(choice, "r")
        topic_names = list(topics.keys())
        
        self.select_topic_frame = ctk.CTkFrame(self.main_frame)
        self.select_topic_frame.grid(column=0, row=1, sticky="nsew", padx=20, pady=20)
        
        self.select_topic_frame.grid_columnconfigure(0, weight=1)
        col = 0
        row = 0
        for i, topic in enumerate(topic_names):
            print(row, col)
            if i % 5 == 0 and i != 0:
                col += 1
                row = 0
            
            self.check_var = ctk.StringVar(value='on')
            self.checkbox = ctk.CTkCheckBox(self.select_topic_frame, 
                                    text=topic,
                                    height=24, 
                                    checkbox_width=24, 
                                    checkbox_height=24,
                                    variable=self.check_var, 
                                    onvalue='on', 
                                    offvalue='off')
            
            self.checkbox.grid(column=col, row=row+1, padx=20, pady=10)
            self.select_topic_frame.grid_columnconfigure(col, weight=1)
            row += 1
        
        self.begin_button = ctk.CTkButton(self.select_topic_frame,
                                    text="Begin",
                                    height=40,
                                    command=self.begin,
                                    font=("Calibre", 20),
                                    fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR),
                                    text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

        self.begin_button.grid(column=0, row=len(topic_names)+2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def remake_frame(self):
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

    def begin(self):
        displayed_topics = self.select_topic_frame.winfo_children()
        for displayed_topic in displayed_topics:
            if "ctkcheckbox" in displayed_topic.winfo_name():
                if displayed_topic.get() == "on":
                    self.selected_topics.append(displayed_topic.cget("text"))
        
        subject = self.optionmenu_var.get()
        data = util.get_choice(subject, "r")
        
        self.create_question_frame()
    
    def create_question_frame(self):
        self.main_frame.destroy() # type: ignore
        self.remake_frame()

        ask_questions.AskQuestionsFrame(self.main_frame, selected_topics=self.selected_topics, subject=self.optionmenu_var.get(), question_index=self.question_index)
        
        self.back_to_home_btn(self.main_frame)

        
    
    

