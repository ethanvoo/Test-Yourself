import customtkinter as ctk
import utility as util
import colors
import json
import choose_quiz

class AskQuestionsFrame:
    def __init__(self, main_frame, selected_topics: list, subject, question_index: int):
        self.main_frame = main_frame
        self.selected_topics = selected_topics
        self.subject = subject
        self.question_index = question_index

        self.data = util.get_choice(self.subject, "r")
        self.all_questions = [question for topic in self.selected_topics for question in self.data.get(topic, [])]
        
        if self.question_index == len(self.all_questions):
            self.end_quiz()
            return

        self.question_dict: dict | str = self.all_questions[self.question_index]
        self.question_index += 1

        self.question = self.question_dict.get("question", '') # type: ignore
        self.answer = self.question_dict.get("answer", '') # type: ignore
        self.answer.lower()

        self.awarded_words = self.question_dict.get("awarded_words", '') #'# type: ignore
        
        self.ask_question_frame = ctk.CTkFrame(main_frame)
        self.ask_question_frame.grid(column=0, row=0, sticky="nsew")
        self.ask_question_frame.columnconfigure(0, weight=1)

        self.question_label = ctk.CTkLabel(self.ask_question_frame, 
                                           text=self.question, 
                                           text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR), 
                                           font=("Calibre", 24))
        
        self.question_label.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        self.enter_answer_var = ctk.StringVar()
        self.enter_answer_entry = ctk.CTkEntry(self.ask_question_frame, textvariable=self.enter_answer_var, placeholder_text="Answer", font=("Calibre", 24))
        self.enter_answer_entry.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.submit_button = ctk.CTkButton(self.ask_question_frame, text="Submit", command=self.submit_button_callback, font=("Calibre", 20), fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))
        self.submit_button.grid(row = 3, column=0, padx=20, pady=20, sticky="ew")
        return

    def submit_button_callback(self):    
        if self.validate_answer():
            self.ask_question_frame.destroy() # type: ignore
            
            self.__init__(self.main_frame, self.selected_topics, self.subject, self.question_index)
            return
        
        if self.awarded_words:
            self.incorrect_answer_label = ctk.CTkLabel(self.ask_question_frame, text=f"Correct Answer: {self.answer}", fg_color='transparent', font=("Calibre", 23), text_color=util.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.incorrect_answer_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
            
            self.awarded_marks_label = ctk.CTkLabel(self.ask_question_frame, text=f"Marks given for {", ".join(self.awarded_words)}.", fg_color='transparent', font=("Calibre", 23), text_color=util.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.awarded_marks_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        else:
            self.incorrect_answer_label = ctk.CTkLabel(self.ask_question_frame, text=f"Correct Answer: {self.answer}", fg_color='transparent', font=("Calibre", 23), text_color=util.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.incorrect_answer_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")


        self.submit_button.configure(text="Next Question", command = lambda: self.__init__(self.main_frame, self.selected_topics, self.subject, self.question_index))
        return
    
    def validate_answer(self) -> bool:
        user_answer: str = util.remove_punctuation(self.enter_answer_var.get().lower().strip())
        print(user_answer, self.awarded_words)
        if self.awarded_words:
            return all(word in user_answer for word in self.awarded_words)
        
        return user_answer == util.remove_punctuation(self.answer.lower())
            
    
    def end_quiz(self):
        self.main_frame.destroy() # type: ignore
        
        return
        