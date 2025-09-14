import customtkinter as ctk
import utility as util
import colors

class AskQuestionsFrame:
    def __init__(self, main_frame, displayed_topics: list, selected_topics: list, back_to_home_btn):
        self.main_frame = main_frame
        self.displayed_topics = displayed_topics
        self.selected_topics = selected_topics
        self.back_to_home_btn = back_to_home_btn

        for i, displayed_topic in enumerate(displayed_topics):
            if i == len(displayed_topics) -1:
                break
            
            selected = displayed_topic.cget("variable")
            if selected.get() == "on":
                self.selected_topics.append(displayed_topic.cget("text"))
        
        
        self.question_frame = ctk.CTkFrame(self.main_frame)
        self.question_frame.pack(fill="both", expand=True, padx=20, pady=20)

        selected_topics_str = ', '.join(self.selected_topics)

        self.back_to_home_btn()

        