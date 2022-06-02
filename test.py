BGCOLOR = '#21325e'
CORRECT_COLOR = '#f1d00a'
WRONG_COLOR = '#3e487a'
BTN_COLOR = '#f0f0f0'

import csv
from tkinter import *
import random

with open('test.csv', 'r', encoding='UTF-8-sig') as file:
    questions = list(csv.reader(file))

answer = 0

def next_question():
    global answer
    
    for i in range(4):
        buttons[i].config(bg=BTN_COLOR)
    
    multi_choice = random.sample(questions, 4)
    answer = random.randint(0, 3)
    cur_question = multi_choice[answer][0]
    
    question_label.config(text=cur_question)
    
    for i in range(4):
        buttons[i].config(text=multi_choice[i][1])

def check_answer(idx):
    idx = int(idx)
    if answer == idx:
        buttons[idx].config(bg=CORRECT_COLOR)
        window.after(1000, next_question)
    else:
        buttons[idx].config(bg=WRONG_COLOR)

window = Tk()
window.title('인수분해 퀴즈')
window.config(padx=50, pady=10, bg=BGCOLOR)

question_label = Label(window, width=40, height=2, text="text",
                       font=('나눔바른펜', 25, 'bold'), bg=BGCOLOR, fg='white')
question_label.pack(pady=30)

buttons = []
for i in range(4):
    btn = Button(window, text=f'{i}번', width=35, height=2, font=('나눔바른펜', 15, 'bold'),
                 bg=BTN_COLOR, command=lambda idx=i: check_answer(idx))
    btn.pack()
    buttons.append(btn)


next_btn = Button(window, text='다음 문제', width=15, height=2,
                  command=next_question,
                  font=('나눔바른펜', 15, 'bold'), bg=CORRECT_COLOR)
next_btn.pack(pady=30)

next_question()

window.mainloop()