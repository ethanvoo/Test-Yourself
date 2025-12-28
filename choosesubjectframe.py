import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import addquestion
import os
import colors
from PIL import Image
from Account_Frame import AccountMenuFrame
import utility as util


class ChooseSubjectFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.subjects: list = util.get_subjects()
        self.matched_topics: list = []
        self.button_list: list = []
        self.Length = 1400

        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0, 1), weight=1)
        self.configure(border_width=5)

        self.TitleBarFrame()
        self.MainChooserFrame()

        self.go_back_button = ctk.CTkButton(self.master,
                                        text="Go Back",
                                        command=self.go_back_button_callback)
        self.go_back_button.grid(column=2,row=2, sticky="ens")

    def MainChooserFrame(self):
        self.MainChooserFrame = ctk.CTkFrame(self, border_width=20)
        self.MainChooserFrame.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan=2) 
        self.MainChooserFrame.grid_rowconfigure(0, weight=0)
        self.MainChooserFrame.grid_columnconfigure((0,1), weight=1)

        self.SubjectSearch()
        self.AddToSubject()

    def SubjectSearch(self):
        self.SubjectSearchFrame = ctk.CTkFrame(self, border_width=20)
        self.SubjectSearchFrame.grid(row=1, column=0, sticky ="nsw", padx=5, pady=5)
        self.SubjectSearchFrame.grid_rowconfigure(1, weight=0)
        self.SubjectSearchFrame.grid_columnconfigure(0, weight=0)

        self.search_bar_var = ctk.StringVar()
        self.search_bar = ctk.CTkEntry(self.SubjectSearchFrame, textvariable=self.search_bar_var)
        self.search_bar.grid( row=0, column=0, columnspan=2, sticky="ensw", padx=5, pady =5)
        self.search_bar_var.trace_add("write", self.search_bar_callback)

        self.display_subject_scrollableframe = ctk.CTkScrollableFrame(self.SubjectSearchFrame, height= 700, width = 600)
        self.display_subject_scrollableframe.grid(row=1, column=0, columnspan=2, padx = 5, pady = 5, sticky="nesw")
        if self.subjects:
            self.display_subject_scrollableframe.grid_rowconfigure([i for i in range(len(self.subjects))], weight=1)
        else:
            self.display_subject_scrollableframe.grid_rowconfigure(0, weight=1)
        self.display_subject_scrollableframe.grid_columnconfigure((0, 1), weight=1)

        self.search_bar_callback()
    
    def AddToSubject(self):
        self.AddToSubject = ctk.CTkFrame(self, border_width= 5)
        self.AddToSubject.grid(row=1, column=1, sticky = "nesw", padx=5, pady=6, columnspan=2)
        self.AddToSubject.grid_rowconfigure(1, weight=1)
        self.AddToSubject.grid_columnconfigure((0, 1), weight=1)

        self.ubject = util.get_subjects()
        self.button_callback(self.ubject[0])

    def TitleBarFrame(self):
        self.TitleBarFrame = ctk.CTkFrame(self)
        self.TitleBarFrame.grid(row=0, column=0,  sticky="new", padx=5, pady=5, columnspan=3)
        self.TitleBarFrame.grid_rowconfigure(0, weight=0)
        self.TitleBarFrame.grid_columnconfigure((0, 1), weight=1)
        
        self.Account_Image_Path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Account.png")


        self.AccountImage = ctk.CTkImage(light_image=Image.open(self.Account_Image_Path),
                                                                dark_image=Image.open(self.Account_Image_Path),
                                                                size=(50, 50))

        self.Account_Button = ctk.CTkButton(self.TitleBarFrame,
                                            height = 20,
                                            width = 20,
                                            text = "",
                                            image = self.AccountImage,
                                            command = self.account_center,
                                            fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                            text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

        self.Title = ctk.CTkLabel(self.TitleBarFrame,
                                height = 10,
                                font = ("Calibre", 23),
                                text = "Test Yourself",
                                text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

                        

        self.Title.grid(row=0, column=0, sticky="ns", padx=10, pady=5,columnspan=3)

        self.Account_Button.grid(row=0, column=0, sticky="nes", padx=20, columnspan = 3)

    def go_back_button_callback(self):
        from start_frame import StartFrame
        self.destroy()
        self.go_back_button.destroy()
        self.start_frame = StartFrame(self.master)
        self.start_frame.grid(row=0, column=0, columnspan=2, sticky="nesw", rowspan=3)
    
    
    
    def search_bar_callback(self, *args):
        search_bar_value = self.search_bar_var.get()
        length = len(search_bar_value)
        self.matched_topics = [s for s in self.subjects if search_bar_value.lower() in s[0:length].lower()]

        for widget in self.display_subject_scrollableframe.winfo_children():
            widget.destroy()  # deleting widget
            self.button_list = []


        for i, subject in enumerate(self.matched_topics):
            
            button = ctk.CTkButton(self.display_subject_scrollableframe, text=subject, fg_color='transparent', border_width=1, height=60, command=lambda s=subject: self.button_callback(s))
            
            button.grid(row=i, column=0, columnspan=2, sticky="ew", pady=10)

            self.button_list.append(button)

    def account_center(self):
        self.destroy
        self.account_menu_frame = AccountMenuFrame(self.master)
        self.account_menu_frame.grid(column=0, row=0, sticky="nsew", padx=20, pady=20, columnspan=3)

    def button_callback(self, subject):
        addquestion.AddQuestionsFrame(self.AddToSubject, subject)
    
    def destroy_elements(self):
        self.destroy()
        self.go_back_button.destroy()

    def add_subject_button_callback(self):
        message = ctk.CTkInputDialog(text="Enter Subject Name:", title="Add Subject")
        Add_Subject_Entry = message.get_input()

        if not Add_Subject_Entry:
            CTkMessagebox(title="Error", message="The subject must have a name!", icon="warning")
            return

        if Add_Subject_Entry.lower() in util.get_subjects():
            CTkMessagebox(title="Error", message="This topic already exists!", icon="warning")
            return
        
        self.destroy_elements() 
        addquestion.AddQuestionsFrame(self.master, Add_Subject_Entry)


        






