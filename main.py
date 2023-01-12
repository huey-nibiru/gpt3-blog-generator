import tkinter as tk
from PIL import Image
from tkinter import filedialog, messagebox
import customtkinter, os, generation


uploaded = False
prompt_fp = ""
def upload():
    global uploaded
    filepath = filedialog.askopenfilename()
    prompt_fp=(filepath)
    generation.gpt3_prompts(prompt_fp)
    uploaded=True
    messagebox.showinfo("Alert","Upload Complete")

download_fp = ""
def generate():
    if uploaded==True:
        filepath = filedialog.askdirectory()
        download_fp=(filepath)
        generation.download_file(download_fp)
        messagebox.showinfo("Alert","Blog Generatopn Complete")






customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk("black")
root.geometry("500x350")
root.title("GPT3 Blog Generator")

frame = customtkinter.CTkFrame(master=root,fg_color="black")
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="GPT3 Blog Generator", font=("Roboto", 24))
label.pack(pady=5, padx=10)

button_image = customtkinter.CTkImage(Image.open("/Users/Yousefmacer/Desktop/MEDIA/plain_white_bg.jpeg"), size=(26, 26))
image_button = customtkinter.CTkButton(master=root, text="Powered by Nibiru",image=button_image)
image_button.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="Upload Prompts", command=upload)
button1.pack(pady=30, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Generate", command=generate)
button2.pack(pady=15, padx=10)

root.mainloop()




