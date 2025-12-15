import customtkinter as ctk

from start_frame import StartFrame

ctk.set_appearance_mode("dark")


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Test Yourself")
        self.geometry("800x600")

        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)


        self.start_frame = StartFrame(self)
        self.start_frame.grid(row=0, column=0, columnspan=2, sticky="nesw", rowspan=3)
        
        

        
    
        

main = Main()
main.mainloop()

