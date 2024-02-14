from tkinter import *
from tkinter import messagebox

class Library():
    def __init__(self, bookname, author, rlsdate, pagenumber):
        self.bookname = bookname
        self.author = author
        self.rlsdate = rlsdate
        self.pagenumber = pagenumber


    def add(self):
        with open("books.txt","a+") as file:
            file.write(f"{self.bookname},{self.author},{self.rlsdate},{self.pagenumber}\n")


    def list(self):
        with open("books.txt","r") as file:
            books = file.read()
            books = books.splitlines()
            for book in books:
                booke = book.split(',')
                data = f"Book Name: {booke[0]}  Author: {booke[1]}\n"
                mytext.insert(END,data)


    def remove(self,bookname):
        with open("books.txt","r") as file:
            lines = file.readlines()
        with open("books.txt","w") as file:
            for line in lines:
                if bookname not in line:
                    file.write(line)


window = Tk()
window.geometry("550x500")
window.title("Library App")
font = ['Ariel', 15, "normal"]
window.resizable(width=False, height=False)

label1 = Label(text="Book Name:", font=font)
label1.place(x=15, y=20)

entry1 = Entry(width=15)
entry1.place(x=105, y=20)

label2 = Label(text="Author:", font=font)
label2.place(x=45, y=70)

entry2 = Entry(width=15)
entry2.place(x=105, y=70)

label3 = Label(text="Release Date:", font=font)
label3.place(y=20, x=270)

entry3 = Entry(width=15)
entry3.place(x=370, y=20)

label4 = Label(text="Page Number:", font=font)
label4.place(y=70, x=265)

entry4 = Entry(width=15)
entry4.place(x=370, y=70)

def clear():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)

def add_button():
    bookname = entry1.get()
    author = entry2.get()
    rlsdate = entry3.get()
    pagenumber = entry4.get()
    if (bookname=="" or author=="" or rlsdate=="" or pagenumber==""):
         messagebox.showwarning(title="Error!", message="Please make sure that you add all the info.")
    else:
        newbook = Library(bookname,author,rlsdate,pagenumber)
        newbook.add()
        messagebox.showinfo(title="Success!",message="Your book is completely added.")
        clear()





def list_button():
    mytext.delete("1.0",END)
    library = Library("","","","")
    library.list()

def remove():
    try:
        booktoremove = entry1.get()
        if(booktoremove == ""):
            messagebox.showwarning(title="Error!",message="Please make sure that you entered a book name.")
        else:
            newlibrary = Library(booktoremove,"","","")
            newlibrary.remove(booktoremove)
            messagebox.showinfo(message="Your book is sucessfully removed!",title="Success!")
            clear()
    except:
        messagebox.showwarning(title="Error!",message="Please make sure that you entered a book name.")


add_button = Button(width=3, height=2, font=font, text="Add",command=add_button)
add_button.place(x=400, y=120)

list_button = Button(width=3, height=2, font=font, text="List",command=list_button)
list_button.place(x=300, y=120)

remove_button = Button(width=5, height=2, font=font, text="Remove",command=remove)
remove_button.place(x=200, y=120)

mytext = Text(width=73, height=23)
mytext.place(x=15, y=185)

window.mainloop()
