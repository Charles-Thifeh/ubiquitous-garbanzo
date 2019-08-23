from tkinter import*
import pyttsx3

engine = pyttsx3.init()

# voice type
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# volume
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)

# rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)


myGui = Tk()
def speech():
    b = a.get()
    engine.say(b)
    engine.runAndWait()


a = StringVar()
myGui.title("NLP presentation - Text-to-Speech")
myGui.geometry("400x400")
myLabel1 = Label(text = 'Enter text', fg = 'black').pack()
text = Entry(textvariable=a).pack()
myButton1 = Button(text='To Speech', fg='black', command=speech).pack()


myGui.mainloop()