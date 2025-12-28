import customtkinter as ctk
import utility as util
import colors
from ask_questions import AskQuestionsFrame

class ChooseQuizFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.selected_topics: list = []
        self.master = master
        self.question_index = 0
        self.subjects: list[str]= util.get_subjects()

        
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure((0, 1), weight=1)

        self.label = ctk.CTkLabel(self, text='Choose Subject:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        init_option_value: str = self.subjects[0] if self.subjects else '<None>'

        self.optionmenu_var = ctk.StringVar(value=init_option_value)
        self.optionmenu = ctk.CTkOptionMenu(self, values=self.subjects,
                                                width=140, height=28,
                                                command=self.optionmenu_callback,
                                                variable=self.optionmenu_var)
        self.optionmenu.grid(column=1, row=0, padx=20, pady=20)
        self.optionmenu_callback(init_option_value)

        self.go_back_button = ctk.CTkButton(self.master,
                                    text="Go Back",
                                    height=40,
                                    command=self.go_back_callback,
                                    font=("Calibre", 20),
                                    fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR),
                                    text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))
        self.go_back_button.grid(column=2, row=2, padx=20, pady=20, sticky="e")
    
    def optionmenu_callback(self, choice):
        if self.optionmenu_var.get() == '<None>':
            return
        
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure((0, 1), weight=1)

        topics = util.get_choice(choice, "r")
        topic_names = list(topics.keys())
        
        self.select_topic_frame = ctk.CTkFrame(self)
        self.select_topic_frame.grid(column=0, row=1, sticky="nsew", padx=20, pady=20, columnspan=2)
        
        self.select_topic_frame.grid_columnconfigure(0, weight=1)
        col = 0
        row = 0
        for i, topic in enumerate(topic_names):
            if i % 5 == 0 and i != 0:
                col += 1
                row = 0
            
            self.checkbox = ctk.CTkCheckBox(self.select_topic_frame, 
                                    text=topic,
                                    height=24, 
                                    checkbox_width=24, 
                                    checkbox_height=24, 
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


        self.begin_button.grid(column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

    def remake_frame(self):
        self.destroy()

    def begin(self):
        displayed_topics = self.select_topic_frame.winfo_children()
        
        checkbox_set: set[str] = set()

        for displayed_topic in displayed_topics:
            if "ctkcheckbox" in displayed_topic.winfo_name() and displayed_topic.get() == "on":
                checkbox_set.add("on")
                self.selected_topics.append(displayed_topic.cget("text"))
                continue
            checkbox_set.add("off")
        
        if all("off" in state for state in checkbox_set):
            error_label = ctk.CTkLabel(self, text="Please select at least one topic", fg_color='transparent', font=("Calibre", 23), text_color=util.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            error_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
            checkbox_set = set()
            return
        
        subject = self.optionmenu_var.get()
        data = util.get_choice(subject, "r")
        
        self.create_question_frame()
    
    def create_question_frame(self):
        self.remake_frame()
        self.go_back_button.destroy()

        ask_questions_frame = AskQuestionsFrame(self.master, selected_topics=self.selected_topics, subject=self.optionmenu_var.get(), question_index=self.question_index, current_score=0)
        ask_questions_frame.grid(row=0, column=0, sticky="nesw", columnspan=3)
    
    def go_back_callback(self):
        from start_frame import StartFrame
        
        self.go_back_button.destroy()
        self.remake_frame()

        self.start_frame = StartFrame(self.master)
        self.start_frame.grid(row=0, column=0, columnspan=2, sticky="nesw", rowspan=3)
        
        

        
    
    

