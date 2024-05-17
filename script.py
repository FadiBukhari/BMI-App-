import customtkinter as tk
from PIL import Image, ImageTk
tk.set_default_color_theme("dark-blue")  
def button_callback():
    print("button clicked")

app = tk.CTk()
app.title("BMI Calculator");
app.geometry("900x600")
app.resizable(width=False,height=False)
frame1=tk.CTkFrame(app,width=400,height=300,border_width=4)

frame1.pack_propagate(False)
frame1.grid(row=1,column=1)

# APP LAYOUT
app.columnconfigure(0,weight=3)
app.columnconfigure(1,weight=2)
app.columnconfigure(2,weight=2)
app.columnconfigure(3,weight=1)

app.rowconfigure(0,weight=1)
app.rowconfigure(1,weight=1)
app.rowconfigure(2,weight=1)

# Title

titleframe=tk.CTkFrame(app,border_width=4,width=400,height=100)
title= tk.CTkLabel(titleframe,text="BMI CALCULATOR",font=("Arial", 20,"bold"))
titleframe.pack_propagate(False)
titleframe.grid(row=0,column=1)

title.place(in_=titleframe, anchor="c", relx=.5, rely=.5)

# RADIO LAYOUTS

radioframe= tk.CTkFrame(app,border_width=4)
radioframe.rowconfigure(0,weight=1)
radioframe.rowconfigure(1,weight=1)


radioframe.grid(row=1,column=0)


def radiobutton_event():
    
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = tk.IntVar(value=0)
radiobutton_1 = tk.CTkRadioButton(radioframe, text="Metric Units",command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = tk.CTkRadioButton(radioframe, text="US Units",command=radiobutton_event, variable= radio_var, value=2)
radiobutton_1.select()
radiobutton_1.grid(row=0,column=0,padx=30,pady=20)
radiobutton_2.grid(row=1,column=0,padx=30,pady=20)


# Image frame

imageframe= tk.CTkFrame(app,border_width=5,height=300)
image = Image.open('images/5.PNG')
image = ImageTk.PhotoImage(image)

imageframe.pack_propagate(False)
image_label = tk.CTkLabel(imageframe,text="", image=image)
image_label.pack(side="bottom",pady=20)
imageframe.grid(row=1,column=2)


# Info image

infoframe= tk.CTkFrame(app,border_width=4,width=200,height=50)
infoframe.pack_propagate(False)
info = tk.CTkLabel(infoframe,text="Status: Obese",font=("Arial", 15,"bold"))
info.pack()
infoframe.grid(row=0,column=2)
info.place(in_=infoframe, anchor="c", relx=.5, rely=.5)



# SLIDERS LAYOUT

fs=tk.CTkFrame(frame1,width=200,height=200,fg_color="transparent")
fs.rowconfigure((0,1,2),weight=1,pad=30)



# INNER SLIDER LAYOUT
fs1=tk.CTkFrame(fs,width=80,height=30)
fs2=tk.CTkFrame(fs,width=80,height=30)
fs3=tk.CTkFrame(fs,width=80,height=30)


fs1.columnconfigure(0,weight=1,minsize=80)
fs1.columnconfigure(1,weight=3)
fs1.columnconfigure(2,weight=1)
fs1.columnconfigure(3,weight=1)

fs2.columnconfigure(0,weight=1,minsize=80)
fs2.columnconfigure(1,weight=3)
fs2.columnconfigure(2,weight=1)
fs2.columnconfigure(3,weight=1)

fs3.columnconfigure(0,weight=1,minsize=80)
fs3.columnconfigure(1,weight=3)
fs3.columnconfigure(2,weight=1)
fs3.columnconfigure(3,weight=1)


fs1.grid(row=0,column=0)
fs2.grid(row=1,column=0)
fs3.grid(row=2,column=0)



def slider_value(v,n):
    if n==1:
        l11.delete("0.0",'end')
        l11.insert('end',int(v))
    elif n==2:
        l22.delete("0.0",'end')
        l22.insert('end',int(v))
        
    elif n==3:
        l33.delete("0.0",'end')
        l33.insert('end',int(v))
        



l1=tk.CTkLabel(fs1,text="Age")
l1.grid(row=0,column=0,padx=10)
s1= tk.CTkSlider(fs1,from_=0,to=100,command=lambda value: slider_value(value,1))
s1.grid(row=0,column=1)
l11=tk.CTkTextbox(fs1,width=38,height=10,state="normal",activate_scrollbars=False)
l11.grid(row=0,column=2,padx=10)
l11.insert("0.0", int(s1.get()))



l2=tk.CTkLabel(fs2,text="Weight")
l2.grid(row=0,column=0,padx=10)
s2= tk.CTkSlider(fs2,from_=10,to=300,command=lambda value: slider_value(value,2))
s2.grid(row=0,column=1)
l22=tk.CTkTextbox(fs2,width=38,height=10,state="normal",activate_scrollbars=False)
l22.grid(row=0,column=2,padx=10)
l22.insert("0.0", int(s2.get()))



l3=tk.CTkLabel(fs3,text="Height")
l3.grid(row=0,column=0,padx=10)
s3= tk.CTkSlider(fs3,from_=10,to=300,command=lambda value: slider_value(value,3))
s3.grid(row=0,column=1)
l33=tk.CTkTextbox(fs3,width=38,height=10,state="normal",activate_scrollbars=False)
l33.grid(row=0,column=2,padx=10)
l33.insert('end', int(s3.get()))



def resetslidervalue():
    s1.set(int(l11.get("0.0",'end')))
    s2.set(int(l22.get("0.0",'end')))
    s3.set(int(l33.get("0.0",'end')))
    
def calc():
    weight=float(l22.get("0.0", "end"))
    height=float(float(l33.get("0.0", "end"))/100)
    bmi= (weight/(height*height))
    print(bmi, height ,weight)
    if bmi>=35:
        image=Image.open("images/5.PNG")
        image = ImageTk.PhotoImage(image)
        image_label.configure(image=image)
        info.configure(text="Status: Extreme Obese")
    elif bmi>=30:
        image=Image.open("images/4.PNG")
        image = ImageTk.PhotoImage(image)
        image_label.configure(image=image)
        info.configure(text="Status: Obese")
    elif bmi>=25:
        image=Image.open("images/3.PNG")
        image = ImageTk.PhotoImage(image)
        image_label.configure(image=image)
        info.configure(text="Status: Overweight")
    elif bmi>=18.5:
        image=Image.open("images/2.PNG")
        image = ImageTk.PhotoImage(image)
        image_label.configure(image=image)
        info.configure(text="Status: Normal")
    elif bmi<18.5:
        image=Image.open("images/1.PNG")
        image = ImageTk.PhotoImage(image)
        image_label.configure(image=image)
        info.configure(text="Status: Underweight")
    if bmi>113:
        info.configure(text="Status: ENOUGHHHHH!!")
    resetslidervalue()
        
    
# BUTTON : )

b1=tk.CTkButton(app,text="Calculate",command=calc)
b1.grid(row=2,column=2,sticky='n')



fs.pack()
fs.place(in_=frame1, anchor="c", relx=.5, rely=.5)

app.mainloop()