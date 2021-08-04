import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

root = tk.Tk()
root.title('text-to-speech')
root.configure(background="blue")
label = tk.Label(root,text="Type here something",font= "arial 25 bold",bg="blue",fg="black")
label.pack()
textbox = tk.Entry(root,width=30,font="arial 20")
textbox.pack()

def speak(text):
    engine.say(text)
    engine.runAndWait()

button= tk.Button(root,text="SPEAK",font="arial 25 bold",bg="white",fg="black",command=lambda:speak(textbox.get()))

button.pack()
root.mainloop()