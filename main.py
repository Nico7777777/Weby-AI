from tkinter import *
import openai
from src.scrappy import extracter
from src.nlp import nlp_clasificator
from src.deploy import weby_deploy
from os import environ
from os import path
from os import mkdir
from dotenv import load_dotenv
import webbrowser

load_dotenv()


openai.api_key = environ.get('OPENAI_SK')
linkId = environ.get('NETLIFY_DEPLOY_ID')

models = openai.Model.list()

isSend = False

# --------------------VARIABLES---------------------
root = Tk()
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

root.title("WebyAI")
lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to WebyAI", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

#---------------------FUNCTIONS---------------------
def send():
    input = e.get()
    send = "You -> " + input
    txt.insert(END, "\n" + send)
    if (nlp_clasificator(input) < 0.3):
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": input},
                                                                                        {"role": "system", "content": "you give me only the html, css and js for my requirement about a website without any messages and comments"}])
        txt.insert(END, "\n" + "Bot -> Your command is done successfully! :)")
        if not path.exists("predeploy"):
            mkdir("predeploy")
        with open(path.join("predeploy", "index.html"), "w+") as f:
            f.write(extracter(chat_completion.choices[0].message.content, "html"))
        css_code = extracter(chat_completion.choices[0].message.content, "css")
        with open(path.join("predeploy", "style.css"), "w+") as f:
            f.write(css_code)
        with open(path.join("predeploy", "styles.css"), "w+") as f:
            f.write(css_code)
        with open(path.join("predeploy", "script.js"), "w+") as f:
            f.write(extracter(chat_completion.choices[0].message.content, "javascript"))
        webbrowser.open(path.join("predeploy", "index.html"))
    else:
        weby_deploy(linkId)
        txt.insert(END, "\n" + "Bot -> Your deployment is done! :)\n\nLink: https://weblyai-website--webyaiexample.netlify.app")
    e.delete(0, END)

#----------------------------------------------------

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
            command=send).grid(row=2, column=1)

def main():
    root.resizable(False, False)
    root.mainloop()


if __name__=="__main__":
    gpt_turbo = models.data[16].id
    main()
