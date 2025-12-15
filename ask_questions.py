import customtkinter as ctk
import utility as util
import colors

from word_question_frame import WordQuestionFrame
from multiple_choice_question_frame import MultipleChoiceQuestionFrame


class AskQuestionsFrame(ctk.CTkFrame):
    def __init__(self, master, selected_topics: list, subject, question_index: int, current_score: int):
        super().__init__(master)
        self.master = master
        self.selected_topics = selected_topics
        self.subject = subject
        self.question_index = question_index
        self.score: int = current_score

        self.data = util.get_choice(self.subject, "r")
        self.all_questions = [question for topic in self.selected_topics for question in self.data.get(topic, [])]
        
        if self.question_index == len(self.all_questions):
            self.end_quiz()
            return
        

        self.question_dict: dict | str = self.all_questions[self.question_index]
        self.question_index += 1

        self.question = self.question_dict.get("question", '') 
        self.answer = self.question_dict.get("answer", '') 
        self.is_multiple_choice: bool = self.question_dict.get("multiple_choice", "")

        self.answer.lower()

        self.awarded_words = self.question_dict.get("awarded_words", '')

        self.question_label = ctk.CTkLabel(self, 
                                           text=self.question, 
                                           text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR), 
                                           font=("Calibre", 24))
        self.question_label.grid(row=0, column=0, padx=20, pady=20)

        if self.is_multiple_choice:
            choices = self.question_dict["choices"]

            self.multiple_choice_question_frame = MultipleChoiceQuestionFrame(self, choices=choices)
            self.multiple_choice_question_frame.grid(row=1, column=0, padx=20, pady=20)
        else:
            self.word_question_frame = WordQuestionFrame(self, answer=self.answer)
            self.word_question_frame.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_button_callback, font=("Calibre", 20), fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))
        self.submit_button.grid(row = 3, column=0, padx=20, pady=20, sticky="ew")
        return

    def submit_button_callback(self):    
        if self.validate_answer():
            if self.is_multiple_choice:
                self.multiple_choice_question_frame.destroy()
            else:
                self.word_question_frame.destroy()
            self.score += 1
            
            self.destroy()
            ask_question_frame = AskQuestionsFrame(self.master, self.selected_topics, self.subject, self.question_index, self.score)
            ask_question_frame.grid(row=0, column=0)
            return
        
        if self.awarded_words:
            self.incorrect_answer_label = ctk.CTkLabel(self, text=f"Correct Answer: {self.answer}", fg_color='transparent', font=("Calibre", 23), text_color=util.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.incorrect_answer_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
            
            self.awarded_marks_label = ctk.CTkLabel(self, text=f"Marks given for {", ".join(self.awarded_words)}.", fg_color='transparent', font=("Calibre", 23), text_color=util.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.awarded_marks_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        else:
            self.incorrect_answer_label = ctk.CTkLabel(self, text=f"Correct Answer: {self.answer}", fg_color='transparent', font=("Calibre", 23), text_color=util.rgb_to_hex(colors.ERROR_TEXT_COLOR))
            self.incorrect_answer_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")


        self.submit_button.configure(text="Next Question", command = lambda: self.__init__(self.master, self.selected_topics, self.subject, self.question_index,current_score=self.score))
        return
    
    def validate_answer(self) -> bool:
        if self.is_multiple_choice:
            user_answer: str = util.remove_punctuation(self.multiple_choice_question_frame.get_answer().lower().strip())
        else:
            user_answer: str = util.remove_punctuation(self.word_question_frame.get_answer().lower().strip())
        
        if self.awarded_words:
            return all(word in user_answer for word in self.awarded_words)
        
        return user_answer == util.remove_punctuation(self.answer.lower())
            
    
    def end_quiz(self):
        widgets = self.winfo_children()
        for widget in widgets:
            widget.destroy()
        score_label = ctk.CTkLabel(self.master,
                                   text=f"Quiz Complete! Your Score: {self.score} / {len(self.all_questions)}",
                                   fg_color='transparent',
                                   font=("Calibre", 30), 
                                   text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))
        score_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=3)
        percentage_label = ctk.CTkLabel(self.master,
                                   text=f"Percentage: {round((self.score / len(self.all_questions)) * 100, 2)}%",
                                   fg_color='transparent',
                                   font=("Calibre", 30), 
                                   text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))
        percentage_label.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=3)

        self.go_back_button = ctk.CTkButton(self.master,
                                    text="Go Back",
                                    height=40,
                                    command=self.go_back_callback,
                                    font=("Calibre", 20),
                                    fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR),
                                    text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))
        self.go_back_button.grid(column=2, row=2, padx=20, pady=20, sticky="e")
        return
    
    def go_back_callback(self):
        from start_frame import StartFrame
        widgets = self.master.winfo_children()
        for widget in widgets:
            widget.destroy()
        self.go_back_button.destroy()
        startframe = StartFrame(self.master)
        startframe.grid(row=0, column=0, columnspan=2, sticky="nesw", rowspan=3)
        