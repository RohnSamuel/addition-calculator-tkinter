#creating gui python addition calculator
from tkinter import *
def addition(x,y):
    try:
        num1=float(rootn1.get())
        num2=float(rootn2.get())
        sum=num1+num2
        ans.configure(text=f'The answer is {sum}')
    except Exception:
        ans.config(text='Please enter a valid number')
#window
root=Tk()
root.title('Addition dupe cal 001')
#label
rootl=Label(text='ADDITION CALCULATOR OF TWO NUMBERS',font=('Papyrus',20))
rootl.pack()

#input
rootl1=Label(text='First number',font=('Papyrus',16))
rootl1.pack()
rootn1=Entry(root)
rootn1.pack(fill='x')
rootl2=Label(text='Second number',font=('Papyrus',16))
rootl2.pack()
rootn2=Entry(root)
rootn2.pack(fill='x')

#calculation button
but=Button(text='Answer',font=('Papyrus',16),command=lambda:addition(rootn1,rootn2))
but.pack(fill='x')
#answer
ans=Label(text='',font=('papyrus',16))
ans.pack()
mainloop()