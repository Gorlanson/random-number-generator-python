
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('600x400+200+100')
root.title("Самый лучший генератор")
backgroundColor = "#555"
root.background = backgroundColor

"""Метка FROM начало"""
label_from = Label(text="FROM", fg="#00ff00", bg="#555")
label_from.place(x=10,y=10)

t_from = Text(height=1,width=15, fg="#00ff00", bg="#555")
t_from.place(x=65, y=10)
"""Метка FROM конец"""

"""Метка TO начало"""
label_from = Label(text="TO", fg="#00ff00", bg="#555")
label_from.place(x=10,y=55)

t_to = Text(height=1,width=15, fg="#00ff00", bg="#555")
t_to.place(x=65, y=55)
"""Метка TO конец"""

"""Метка COUNT начало"""
label_count = Label(text="COUNT", fg="#00ff00", bg="#555")
label_count.place(x=10,y=100)

t_count = Text(height=1,width=15, fg="#00ff00", bg="#555")
t_count.place(x=65, y=100)
"""Метка COUNT конец"""

"""Вывод наших чисел начало"""
t_numbers = Text(height=5, width=60, fg="#00ff00", bg="#555")
t_numbers.place(x=10,y=200)
t_numbers.config(state=DISABLED)
"""Вывод наших чисел конец"""

"""Кннопка CLEAR начало"""
def ClickClear(event):
    t_numbers.config(state=NORMAL)
    t_numbers.delete('1.0',END)
    t_from.delete('1.0', END)
    t_to.delete('1.0', END)
    t_count.delete('1.0', END)
    t_numbers.config(state=DISABLED)

clear = Button(text="CLEAR", bg="#555", fg="#00ff00", padx="15", pady="6", font="15")
clear.bind("<Button-1>", ClickClear)
clear.place(x=200, y=150)
"""Кннопка CLEAR конец"""

"""Кннопка GENERATE начало"""
from random import randint

def ClickGen(event1):
    t_numbers.config(state=NORMAL)
    t_numbers.delete('1.0', END)
    if len(t_from.get(1.0, END)) > 8 or len(t_to.get(1.0, END)) > 8:
        messagebox.showinfo("Ошибка", "Вводите чичла поменьше")
        sys.exit()
    else:
        if len(t_count.get(1.0, END)) > 4:
            messagebox.showinfo("Ошибка", "Вводите чичла поменьше")
            sys.exit()
        else:
            if re.match("^[0-9 ]+$", t_from.get(1.0, END)) and re.match("^[0-9 ]+$", t_to.get(1.0, END)):
                if re.match("^[0-9 ]+$", t_count.get(1.0, END)):
                        if int(t_from.get(1.0, END))>int(t_to.get(1.0, END)):
                            messagebox.showinfo("Ошибка", "Введите числа от меньшего к большему")
                            t_from.delete('1.0', END)
                            t_to.delete('1.0', END)
                            t_count.delete('1.0', END)
                        else:
                            ch1 = int(t_from.get(1.0, END))
                            ch2 = int(t_to.get(1.0, END))

                            i=0
                            c=int(t_count.get(1.0, END))
                            vivod = ""

                            while i < c:
                                rez = randint(ch1, ch2)
                                vivod=vivod+str(rez)+" "
                                i = i+1
                            t_numbers.insert(1.0, vivod)
                            t_numbers.config(state=DISABLED)
                else:
                    messagebox.showinfo("Ошибка", "Вводите только числа >0")
            else:
                messagebox.showinfo("Ошибка", "Вводите только числа >0")


gen = Button(text="GENERATE", bg="#555", fg="#00ff00", padx="15", pady="6", font="15")
gen.bind("<Button-1>", ClickGen)
gen.place(x=10, y=150)
"""Кннопка GENERATE конец"""

root.mainloop()