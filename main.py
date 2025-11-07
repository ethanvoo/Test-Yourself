import customtkinter as ctk
import utility as util
import colors

from start_frame import StartFrame

ctk.set_appearance_mode("dark")


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Test Yourself")
        self.geometry("600x600")

        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)


        self.start_frame = StartFrame(self)
        self.start_frame.grid(row=0, column=0, columnspan=2, sticky="nesw", rowspan=3)
        
        

    def back_to_home_btn(self):
        self.back_to_home_button = ctk.CTkButton(self.main_frame, text="Back to Home", width=75, height=24, command=self.back_to_home_btn_callback)
        self.back_to_home_button.grid(column=0, padx=20, pady=20, sticky="w")
    
    def back_to_home_btn_callback(self):
        self.remake_frame()
        self.start_menu()
        
    
        

main = Main()
main.mainloop()

