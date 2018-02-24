from tkinter import *
from functools import partial as pto
from tkinter.messagebox import showinfo, showwarning, showerror

WARN = "warn"
CRIT = "crit"
REGU = "regu"

SIGNS = {
    "do not enter": CRIT,
    "railroad crossing": WARN,
    "55\nspeed limit": REGU,
    "wrong way": CRIT,
    "merging traffic": WARN,
    "one way": REGU,
}


def critCB(): return showerror("Error", "Error Button Pressed!")
# critCB = lambda : print("run")


def warnCB(): return showwarning("Warning", "Warning Button Pressed!")


def infoCB(): return showinfo("Info", "Info Button Pressed!")


top = Tk()
top.title("Road Signs")
Button(top, text="QUIT", command=top.quit, bg="red", fg="white").pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg="white", fg="red")
WarnButton = pto(MyButton, command=warnCB, bg="goldenrod1")
ReguButton = pto(MyButton, command=infoCB, bg="white")

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = "%sButton(text=%r%s).pack(fill=X, expand=1)" % (
        signType.title(), eachSign, ".upper()" if signType == CRIT else ".title()")
    eval(cmd)

top.mainloop()
