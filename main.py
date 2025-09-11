import customtkinter as ctk
import json 

root = ctk.CTk()
root.geometry("600x600")
root.title("Test Yourself")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

MAIN_BUTTON_COLOR = (0, 122, 204)
MAIN_BUTTON_HOVER_COLOR = (21, 143, 209)
MAIN_TEXT_COLOR = (255, 255, 255)

selected_topics: list = []
add_selected_subjects: list = []
topic_add_to: str = ''
subject_add_to: str = ''

def add_topic(value):
    print(value)

def get_choice(choice):
    if choice == "Music":
        with open("music.json", "r") as f:
            return json.load(f)
    elif choice == "Computer Science":
        with open("computer_science.json", "r") as f:
            return json.load(f)
    elif choice == "Chemistry":
        with open("chemistry.json", "r") as f:
            return json.load(f)

def optionmenu_callback(choice):
    global select_topic_frame
    select_topic_frame = ctk.CTkFrame(main_frame)
    select_topic_frame.grid(column=0, row=1)
    topics = get_choice(choice)
    topic_names = list(topics.keys()) # type: ignore
    
    for i, topic in enumerate(topic_names):
        check_var = ctk.StringVar(value='on')
        checkbox = ctk.CTkCheckBox(select_topic_frame, text=topic, width=100, height=24, checkbox_width=24, checkbox_height=24,
                                             variable=check_var, onvalue='on', offvalue='off')
        checkbox.grid(column=0, row=i, padx=20, pady=10)
    
    begin_button = ctk.CTkButton(select_topic_frame, text="Begin", width=100, height=24, command=begin)
    begin_button.grid(column=0, row=len(topic_names), padx=20, pady=10)
    back_to_home_btn()

def begin():
    displayed_topics = select_topic_frame.winfo_children()
    
    for i, displayed_topic in enumerate(displayed_topics):
        if i == len(displayed_topics) -1:
            break
        selected = displayed_topic.cget("variable")
        if selected.get() == "on":
            selected_topics.append(displayed_topic.cget("text"))
    main_frame.destroy()
    remake_frame()
    question_frame = ctk.CTkFrame(main_frame)
    question_frame.pack(fill="both", expand=True, padx=20, pady=20)

    selected_topics_str = ', '.join(selected_topics)

    title = ctk.CTkLabel(question_frame, text=f'Questions on {selected_topics_str}', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
    title.pack(padx=20, pady=20)

def select_subject():
    selection_frame.destroy()
    global select_subject_frame
    select_subject_frame = ctk.CTkFrame(main_frame)
    select_subject_frame.grid(column=0, row=0)

    label = ctk.CTkLabel(select_subject_frame, text='Choose Subject:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
    label.grid(row=0, column=0, padx=20, pady=20)

    optionmenu_var = ctk.StringVar(value='<None>')
    optionmenu = ctk.CTkOptionMenu(select_subject_frame, values=['Chemistry', 'Computer Science', "Music"],
                                            width=140, height=28,
                                            command=optionmenu_callback,
                                            variable=optionmenu_var)
    optionmenu.grid(column=1, row=0, padx=20, pady=20)

    back_to_home_btn()

def topic_optionmenu_callback(value):
    global topic_add_to
    topic_add_to = value

def subject_optionmenu_callback(value):
    global subject_add_to, topic_add_to
    subject_add_to = value
    topic_add_to = ''
    choose_topic_label = ctk.CTkLabel(add_questions_frame, text='Choose Topic:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
    choose_topic_label.grid(row=1, column=0, padx=20, pady=20)

    topics = get_choice(value)
    topics_list = list(topics.keys()) # type: ignore

    topic_optionmenu_var = ctk.StringVar(value='<None>')
    topic_optionmenu = ctk.CTkOptionMenu(add_questions_frame, values=topics_list,
                                            width=140, height=28,
                                            command=topic_optionmenu_callback,
                                            variable=topic_optionmenu_var)
    topic_optionmenu.grid(column=1, row=1, padx=20, pady=20)
    
    add_question_label = ctk.CTkLabel(add_questions_frame, text='Add Question:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
    add_question_label.grid(row=2, column=0, padx=20, pady=20)

    add_question_entry = ctk.CTkEntry(add_questions_frame, width=280, height=28, placeholder_text='Question')
    add_question_entry.grid(column=1, row=2, padx=20, pady=20)

    add_answer_label = ctk.CTkLabel(add_questions_frame, text='Add Answer:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
    add_answer_label.grid(row=3, column=0, padx=20, pady=20)

    add_answer_entry = ctk.CTkEntry(add_questions_frame, width=280, height=28, placeholder_text='Answer')
    add_answer_entry.grid(column=1, row=3, padx=20, pady=20)

    add_question_button = ctk.CTkButton(add_questions_frame, text="Add Question", width=100, height=24, command=create_question)
    add_question_button.grid(column=0, padx=20, pady=20)

def add_questions():
    selection_frame.destroy()
    global add_questions_frame
    global select_subject_frame
    add_questions_frame = ctk.CTkFrame(main_frame)
    add_questions_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    

    choose_subject_label = ctk.CTkLabel(add_questions_frame, text='Choose Subject:', width=30, height=28, fg_color='transparent', font=("Calibre", 23))
    choose_subject_label.grid(row=0, column=0, padx=20, pady=20)

    subject_optionmenu_var = ctk.StringVar(value='<None>')
    subject_optionmenu = ctk.CTkOptionMenu(add_questions_frame, values=['Chemistry', 'Computer Science', "Music"],
                                            width=140, height=28,
                                            command=subject_optionmenu_callback,
                                            variable=subject_optionmenu_var)
    subject_optionmenu.grid(column=1, row=0, padx=20, pady=20)

    back_to_home_btn()


def create_question():
    displayed_widgets = add_questions_frame.winfo_children()
    for i, displayed_widget in enumerate(displayed_widgets):
        if displayed_widget.winfo_class() == "CTkRadioButton":
            selected = displayed_widget.cget("variable")
            if selected.get() == "on":
                add_selected_subjects.append(displayed_widget.cget("text"))

def back_to_home_btn_callback():
    main_frame.destroy() # type: ignore
    start()

def back_to_home_btn():
    back_to_home_btn = ctk.CTkButton(main_frame, text="Back to Home", width=75, height=24, command=back_to_home_btn_callback)
    back_to_home_btn.grid(column=0, padx=20, pady=20)

def fade_effect(widget, attribute, start_color, end_color, steps=10, delay=10):
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color

    dr = (r2 - r1) / steps
    dg = (g2 - g1) / steps
    db = (b2 - b1) / steps

    for i in range(steps + 1):
        r = int(r1 + dr * i)
        g = int(g1 + dg * i)
        b = int(b1 + db * i)
        print(r, g, b)
        color = _from_rgb((r, g, b))
        widget.configure(**{attribute: color})
        widget.update()
        widget.after(delay)

def on_hover_button(event, widget=None):
    print("Hover")
    fade_effect(widget=widget, attribute="fg_color", start_color=MAIN_BUTTON_COLOR, end_color=MAIN_BUTTON_HOVER_COLOR, steps=10, delay=30)

def on_leave_button(event, widget=None):
    print("Unhover")
    fade_effect(widget=widget, attribute="fg_color", start_color=MAIN_BUTTON_HOVER_COLOR, end_color=MAIN_BUTTON_COLOR, steps=10, delay=30)

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb 

def start():
    remake_frame()
    global selection_frame, select_subject_button, add_questions_button
    
    selection_frame = ctk.CTkFrame(main_frame)
    selection_frame.columnconfigure(0, weight=1)
    selection_frame.rowconfigure((1, 2), weight=1)
    selection_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    title = ctk.CTkLabel(selection_frame, 
                         text='Test Yourself', 
                         width=30, height=28, 
                         fg_color='transparent', 
                         font=("Calibre", 40),
                         text_color=_from_rgb(MAIN_TEXT_COLOR))
    title.grid(row=0, column=0, padx=20, pady=20)

    select_subject_button = ctk.CTkButton(selection_frame, 
                                          text="Select Subject",
                                          command=select_subject, 
                                          font=("Calibre", 23), 
                                          fg_color=_from_rgb(MAIN_BUTTON_COLOR), 
                                          text_color=_from_rgb(MAIN_TEXT_COLOR))
    
    select_subject_button.grid(column=0, row=1, padx=20, pady=20, sticky="nesw")
    select_subject_button.bind("<Enter>", lambda x: on_hover_button(x, widget=select_subject_button))
    select_subject_button.bind("<Leave>", lambda x: on_leave_button(x, widget=select_subject_button))

    add_questions_button = ctk.CTkButton(selection_frame, 
                                         text="Add Questions",
                                         command=add_questions, 
                                         font=("Calibre", 23), 
                                         fg_color=_from_rgb(MAIN_BUTTON_COLOR), 
                                         text_color=_from_rgb(MAIN_TEXT_COLOR))
    
    add_questions_button.grid(column=0, row=2, padx=20, pady=20, sticky="nesw")
    add_questions_button.bind("<Enter>", lambda x: on_hover_button(x, widget=add_questions_button))
    add_questions_button.bind("<Leave>", lambda x: on_leave_button(x, widget=add_questions_button))

def remake_frame():
    global main_frame
    main_frame = ctk.CTkFrame(root)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid(row=0, column=0, sticky="nsew")

start()
root.mainloop()