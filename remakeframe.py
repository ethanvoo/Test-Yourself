import customtkinter as ctk

def remake_frame(root):
    main_frame = ctk.CTkFrame(root)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid(row=0, column=0, sticky="nsew")