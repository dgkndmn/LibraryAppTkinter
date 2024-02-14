from tkinter import *

window = Tk()
window.geometry("550x500")
window.title("Library App")
font = ['Ariel',15,"normal"]
window.resizable(width=False,height=False)

label1 = Label(text="Book Name:",font=font)
label1.place(x=15,y=20)

entry1 = Entry(width=15)
entry1.place(x=105,y=20)

label2 = Label(text="Author:",font=font)
label2.place(x=45,y=70)

entry2 = Entry(width=15)
entry2.place(x=105,y=70)

label3 = Label(text="Release Date:",font=font)
label3.place(y=20,x=270)

entry3 = Entry(width=15)
entry3.place(x=370,y=20)

label4 = Label(text="Page Number:",font=font)
label4.place(y=70,x=265)

entry4 = Entry(width=15)
entry4.place(x=370,y=70)

add_button = Button(width=3,height=2,font=font,text="Add")
add_button.place(x=400,y=120)

list_button = Button(width=3,height=2,font=font,text="List")
list_button.place(x=300,y=120)

remove_button = Button(width=5,height=2,font=font,text="Remove")
remove_button.place(x=200,y=120)

frame = Frame(window,width=520,height=300,bg="lightgray")
frame.place(x=15,y=190)


window.mainloop()
