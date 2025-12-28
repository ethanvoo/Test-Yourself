import customtkinter as ctk
import utility as util
import colors
import os
import numpy as np
from PIL import Image
from choose_quiz import ChooseQuizFrame
from choosesubjectframe import ChooseSubjectFrame
from Account_Frame import AccountMenuFrame
import ctkchart


class StartFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.Length = 1400

        self.rowconfigure((0,1), weight=0)
        self.columnconfigure((0, 1), weight=1)
        self.configure(border_width=5)

        self.TitleBarFrame()
        self.GraphFrame()
        self.AskQuestionsFrame()
        self.ChooseSubjectFrame()
        

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
     
    
    def GraphFrame(self):
        self.GraphFrame = ctk.CTkFrame(self)
        self.GraphFrame.grid(row=1, column=2,  sticky="new", padx=(5,10), pady=5)
        self.GraphFrame.grid_rowconfigure(0, weight=0)
        self.GraphFrame.grid_columnconfigure((0, 1), weight=1)

        self.GraphPointMapper()

        self.Graph = ctkchart.CTkLineChart(
            master=self.GraphFrame,  # Set the master as the root window
            x_axis_values=(self.Day4,self.Day3,self.Day2,self.Day1,self.Day0),  # X-axis values
            y_axis_values=(0, 100),  # Y-axis values (range)
            y_axis_label_count=10, # set y axis labels count to 10
            x_axis_data_position= "side",
            y_axis_data= "Score",
            x_axis_data= "Date",
            height = 400,
            width = 500
        )

        self.Graph.grid(row=0, column=0, padx=20, columnspan = 3)

        # Create a line for the line chart
        self.line = ctkchart.CTkLine(
            master=self.Graph,  # Set the master as the line chart
            size=5,  # Set the line size to 5
            fill="disabled" # enable line fill
        )  

        self.Graph.show_data(line=self.line, data=self.xPoints)

    def AskQuestionsFrame(self):   
        self.AskQuestionsFrame = ctk.CTkFrame(self)
        self.AskQuestionsFrame.grid(row=1, column=0, padx=5, pady=5)
        self.AskQuestionsFrame.grid_rowconfigure(0, weight=0)
        self.AskQuestionsFrame.grid_columnconfigure((0, 1), weight=0)

        self.select_subject_button = ctk.CTkButton(self.AskQuestionsFrame, 
                                          text="Select Subject",
                                          command=self.select_subject, 
                                          font=("Calibre", 23), 
                                          height = 400,
                                          width = 500,
                                          fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                          text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

        self.select_subject_button.grid(column=0, row=0, columnspan=2)

    def ChooseSubjectFrame(self):   
        self.ChooseSubjectFrame = ctk.CTkFrame(self)
        self.ChooseSubjectFrame.grid(row=1, column=1, padx=5, pady=5)
        self.ChooseSubjectFrame.grid_rowconfigure(0, weight=0)
        self.ChooseSubjectFrame.grid_columnconfigure((0, 1), weight=0)

        self.select_subject_button = ctk.CTkButton(self.ChooseSubjectFrame, 
                                          text="Add Questions to a Topic!",
                                          command=self.add_questions, 
                                          font=("Calibre", 23), 
                                          height = 400,
                                          width = 500,
                                          fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                          text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

        self.select_subject_button.grid(column=0, row=0, columnspan=2)


    def GraphPointMapper(self):
        self.Day4 = "24/11"
        self.Day3 = "25/11"
        self.Day2 = "26/11"
        self.Day1 = "27/11"
        self.Day0 = "28/11"

        #the first extra point is for the point (p1,(x=0))
        #the array def(): [p1,p2,p3,p4,p5,p6]
        self.xPoints = [0,45,52,67,73,89]

    def account_center(self):
        self.destroy
        self.account_menu_frame = AccountMenuFrame(self.master)
        self.account_menu_frame.grid(column=0, row=0, sticky="nsew", padx=20, pady=20, columnspan=3)

    def add_questions(self):
        self.destroy()
        self.choose_subject_frame = ChooseSubjectFrame(self.master)
        self.choose_subject_frame.grid(column=0, row=0, sticky="nesw", padx=20, pady=20, columnspan=3)

    def select_subject(self):
        self.destroy()
        self.choosequiz_frame = ChooseQuizFrame(self.master)
        self.choosequiz_frame.grid(column=0, row=0, sticky="nsew", padx=20, pady=20, columnspan=3)
    
    def remake_frame(self):
        self.destroy()

        '''
            self.GraphImage = ctk.CTkImage(light_image=Image.open("Images/ScoreGraph.png"),
                                        dark_image=Image.open("Images/ScoreGraph.png"),
                                        size=(600, 350))

            self.GraphLabel = ctk.CTkLabel(self.GraphFrame, image=self.GraphImage, text="") 

            self.GraphLabel.grid(row=0, column=0, sticky="nes", padx=20, columnspan = 3)
            
        def GraphMaker(self):
            self.GraphPointMapper()
            self.Xaxis = [self.Xplot1, self.Xplot2, self.Xplot3, self.Xplot4, self.Xplot5]
            self.Yaxis = [self.Yplot1, self.Yplot2, self.Yplot3, self.Yplot4, self.Yplot5]

            plt.figure(figsize=(8, 5))
            fig, ax = plt.subplots()

            #ts is just the colours of the graph
            ax.spines['top'].set_color('#333333')
            ax.spines['bottom'].set_color('#D3D3D3')
            ax.spines['left'].set_color('#D3D3D3')
            ax.spines['right'].set_color('#333333')
            ax.tick_params(colors='#D3D3D3', which='both')
            ax.set_xlabel('X Value', color='#D3D3D3', fontsize=14)
            ax.set_ylabel('Y Value', color='#D3D3D3', fontsize=14)
            ax.set_facecolor('#333333') 
            fig.patch.set_facecolor('#333333')


            plt.plot(self.Xaxis, self.Yaxis, color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), marker = "o", markersize = 5) 
            plt.xlabel('Date')
            plt.ylabel('Score')
            plt.savefig('ScoreGraph.png', dpi=300, bbox_inches='tight') 
            plt.close()
        '''
        '''
        self.title = ctk.CTkLabel(self, 
                        text='Test Yourself', 
                        width=30, height=28, 
                        fg_color='transparent', 
                        font=("Calibre", 40),
                           text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

        self.title.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        self.select_subject_button = ctk.CTkButton(self, 
                                          text="Select Subject",
                                          command=self.select_subject, 
                                          font=("Calibre", 23), 
                                          fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                          text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

        self.select_subject_button.grid(column=0, row=1, padx=20, pady=20, sticky="nesw", columnspan=2)

        self.add_questions_button = ctk.CTkButton(self, 
                                          text="Add Questions",
                                          command=self.add_questions, 
                                          font=("Calibre", 23), 
                                          fg_color=util.rgb_to_hex(colors.MAIN_BUTTON_COLOR), 
                                          text_color=util.rgb_to_hex(colors.MAIN_TEXT_COLOR))

        self.add_questions_button.grid(column=0, row=2, padx=20, pady=20, sticky="nesw", columnspan=2)

    def add_questions(self):
        self.destroy()
        self.choose_subject_frame = ChooseSubjectFrame(self.master)
        self.choose_subject_frame.grid(column=0, row=0, sticky="nesw", padx=20, pady=20, columnspan=3)

    def select_subject(self):
        self.destroy()
        self.choosequiz_frame = ChooseQuizFrame(self.master)
        self.choosequiz_frame.grid(column=0, row=0, sticky="nsew", padx=20, pady=20, columnspan=3)
        '''