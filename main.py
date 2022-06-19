from tkinter import Entry

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading


engine=pp.init()

voices=engine.getProperty('voices')
print(voices)

engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My bot")

convo = [
    'hello'
    'hello rospinot !',
    'What is your name ?',
    'My name is rospinot,i am created by Pranjal',
    'What is Rospinot ?',
    'Robotics Operating Systems using Python Intelligence with Node Open Technology',
    'Hello sir ?',
    'hello Dr. Amit Srivastava sir',
    'In which language you talk ?',
    'I am mostly talk in English and hindi'
    'tell me something about Pranjal?',
    'I am Pranjal Pandey.',
    'one good friend of pranjal'
    'hai na Nikita Mishra!'
]
trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

# answer = bot.get_response("What is your name ?")
# print(answer)
# print("Talk to bot")
# while True:
#    query=input()
#     if query=='exit':
#        break
#    answer=bot.get_response(query)
#    print("bot :",answer)




main = Tk()

main.geometry("500x600")

main.title("My Chat Bot")
img = PhotoImage(file='bot2.png')

photoL = Label(main, image=img)
photoL.pack(pady=5)

#take query: it takes audio as input froem user and convert into string

def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_rospinot_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_rospinot_bot():
    query=textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you :" + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot :" + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame,width=80,height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

#Creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn=Button(main,text="Ask from Rospinot bot",font=("Verdana",20),command=ask_from_rospinot_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()




#going to bind main window with enter key

main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()



t=threading.Thread(target=repeatL)

t.start()

main.mainloop()




