import customtkinter as ctk
import utility as util
import colors
import addquestions, choose_quiz
import os

file_path = "LeaderBoard.csv"
if not os.path.exists(file_path):
    file = open("LeaderBoard.csv","w")
    file.write("Random Dice Leader board!\n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.write(" , \n")
    file.close()


root = ctk.CTk()
root.geometry("600x600")
root.title("Test Yourself")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

selected_topics: list = []
add_selected_subjects: list = []
topic_add_to: str = ''
subject_add_to: str = ''
            
def back_to_home_btn_callback():
    main_frame.destroy() # type: ignore
    start()

def back_to_home_btn():
    back_to_home_btn = ctk.CTkButton(main_frame,
                                     text="Back to Home",
                                     width=75, height=24,
                                     command=back_to_home_btn_callback)
    
    back_to_home_btn.grid(column=0, padx=20, pady=20, sticky="w")

 
def start():
    remake_frame(root)
    
    
    selection_frame = ctk.CTkFrame(main_frame)
    selection_frame.columnconfigure(0, weight=1)
    selection_frame.rowconfigure((1, 2), weight=1)
    selection_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    title = ctk.CTkLabel(selection_frame, 
                         text='Test Yourself', 
                         width=30, height=28, 
                         fg_color='transparent', 
                         font=("Calibre", 40),
                         text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))
    
    title.grid(row=0, column=0, padx=20, pady=20)


    select_subject_button = ctk.CTkButton(selection_frame, 
                                          text="Select Subject",
                                          command=select_subject, 
                                          font=("Calibre", 23), 
                                          fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                          text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))
 
    select_subject_button.grid(column=0, row=1, padx=20, pady=20, sticky="nesw")


    add_questions_button = ctk.CTkButton(selection_frame, 
                                         text="Add Questions",
                                         command=add_questions, 
                                         font=("Calibre", 23), 
                                         fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                         text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

    add_questions_button.grid(column=0, row=2, padx=20, pady=20, sticky="nesw")

def add_questions():
    global main_frame
    main_frame.destroy() # type: ignore
    remake_frame(root)
    main_frame = ctk.CTkFrame(root)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid(row=0, column=0, sticky="nsew")
    addquestions.AddQuestionsFrame(main_frame)
    back_to_home_btn()

def select_subject():
    main_frame.destroy() # type: ignore
    remake_frame(root)
    choose_quiz.ChooseQuizFrame(main_frame, root, back_to_home_btn)
    back_to_home_btn()
    
def remake_frame(root):
    global main_frame
    main_frame = ctk.CTkFrame(root)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid(row=0, column=0, sticky="nsew")

start()
root.mainloop()