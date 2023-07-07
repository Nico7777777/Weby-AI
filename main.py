from tkinter import *
import openai


openai.api_key="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"

models = openai.Model.list()

# --------------------VARIABLES---------------------
root = Tk()
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

root.title("WebyAI")
lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

#---------------------FUNCTIONS---------------------
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
    user = e.get().lower()
    txt.insert(END, "\n" + "Bot -> " + chat_completion.choices[0].message.content)
    e.delete(0, END)

def output_data():
    with open("modele.txt", 'w') as f:
        f.write(str(models))

def output_engines():
    with open("motoare.txt", 'w') as g:
        for alpha in range(len(models.data)):
            g.write( str(alpha+1) + '. ' + str(models.data[alpha].id) + '\n')
#----------------------------------------------------

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
            command=send).grid(row=2, column=1)

def main():
    root.mainloop()


if __name__=="__main__":
    #output_data()
    #output_engines()
    gpt_turbo = models.data[16].id # gpt-3.5-turbo
    #print()
    main()
