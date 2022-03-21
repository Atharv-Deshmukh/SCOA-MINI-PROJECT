from tkinter import *
from tkinter import filedialog, messagebox
from Fuzzy import *

window = Tk()
window.title("Tipping Solution")
path_to_save = ""

def btnClicked():
    quality_input = int(quality_entry.get())
    service_input = int(service_entry.get())

    if (service_input > 10) or (quality_input >10):
        messagebox.showerror(title="Incorrect Ratings", message="Ratings must be 0 to 10")
    else:
        tip_output = str(compute_tip(service_input, quality_input))
        messagebox.showerror(title="Your Tip should be", message=tip_output[0:5])

window.geometry("862x519")
window.configure(bg="#3A7FF6")
canvas = Canvas(window,bg="#3A7FF6",height=519,width=862,bd=0, highlightthickness=0,relief="ridge")
canvas.place(x=0,y=0)
canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#FCFCFC",outline="")
canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#FCFCFC",outline="")

text_box_bg = PhotoImage(file=f"images/TextBox_Bg.png")

service_rating = canvas.create_image(650.5,167.5,image=text_box_bg)
food_quality = canvas.create_image(650.5,248.5,image=text_box_bg)

service_entry = Entry(bd=0,bg="#F6F7F9",highlightthickness=0)
service_entry.place(x=490.0,y=137+25,width=321.0,height=35)

quality_entry = Entry(bd=0,bg="#F6F7F9",highlightthickness=0)
quality_entry.place(x=490.0,y=218+25,width=321.0,height=35)


canvas.create_text(519.0,156.0,text="Service",fill="#515486",font=("Arial-BoldMT",int(13.0)))
canvas.create_text(550.0,234.5,text="Food Quality",fill="#515486",font=("Arial-BoldMT",int(13.0)))
canvas.create_text(646.0,88.0,text="Give your Ratings",fill="#515486",font=("Arial-BoldMT",int(22.0)))

title = Label(text="Welcome to\n""Tipping Problem Solution", bg="#3A7FF6",fg="white",font=("Arial-BoldMT",int(20.0)))
title.place(x=27.0,y=120.0)

info_text = Label(text="It is a fuzzy control system which\n"
                   "computes how you might choose to\n"
                   "tip at a restaurant.\n\n"

                   "When tipping, you consider the\n"
                   "service and food quality,\n"
                   "rated between 0 and 10.\n\n",
                   
              bg="#3A7FF6",fg="white",justify="left",font=("Georgia",int(16.0)))

info_text.place(x=27.0,y=200.0)

generate_btn_img = PhotoImage(file="./images/generate.png")
generate_btn = Button(image=generate_btn_img, borderwidth=0, highlightthickness=0, command=btnClicked, relief="flat")
generate_btn.place(x=557, y=300, width=180, height=55)
window.resizable(False, False)
window.mainloop()