import sys
from tkinter import *
import os
import pandas as pd
import random

window = Tk()
window.title("Typing Speed Test")
window.config(width=500, height=400)

df = pd.read_csv('static/1200_words.csv')
word_list = random.sample(list(df['Word']),100)

current_word_index = 0
correct_words = 0
incorrect_words = 0
characters_typed = 0
correct_characters = 0

time_remaining = 60
timer_started = False
timer_id = None

## Set up GUI
timer_label = Label(window,
                    text="Time: 60",
                    font=("Arial", 18, "bold")
                    )
timer_label.grid(row=0, column=0, pady=10)

sample_text = Text(window,
                    width=40,
                    height=10,
                    bg='light blue',
                    fg='black',
                    wrap=WORD,
                    font=('Courier', 20),
                   relief='flat',
                   padx=10,
                   pady=10)
sample_text.grid(row=1, column=0, padx=10, pady=10)

sample_text.insert("1.0", " ".join(word_list))

word_positions = []

position = 0

for word in word_list:
    start = f"1.{position}"
    end = f"1.{position + len(word)}"
    word_positions.append((start, end))
    position += len(word) + 1

sample_text.config(state="disabled")
sample_text.tag_config("current",
                       background="green",
                       foreground="black")
sample_text.tag_config("correct",
                       foreground="green")
sample_text.tag_config("incorrect",
                       foreground="red")

def highlight_word(index):
    sample_text.config(state='normal')
    sample_text.tag_remove("current", "1.0", END)
    if index < len(word_positions):
        start, end = word_positions[index]
        sample_text.tag_add("current", start, end)
        sample_text.see(start)
    sample_text.config(state="disabled")

highlight_word(current_word_index)

def check_word(event):
    global current_word_index, correct_words, incorrect_words, characters_typed, correct_characters

    typed = user_word.get().strip()
    expected = word_list[current_word_index]
    characters_typed += len(typed)

    sample_text.config(state="normal")

    start, end = word_positions[current_word_index]

    matching = 0
    for t, e in zip(typed, expected):
        if t == e:
            matching += 1
    correct_characters += matching

    if typed == expected:
        sample_text.tag_add("correct", start, end)
        correct_words += 1
    else:
        sample_text.tag_add("incorrect", start, end)
        incorrect_words += 1

    update_stats()
    current_word_index += 1

    if current_word_index < len(word_list):
        highlight_word(current_word_index)
    else:
        user_word.config(state="disabled")

    user_word.delete(0, END)

    return "break"

user_word = Entry(textvariable=StringVar())
user_word.grid(row=2, column=0)

stats_label = Label(window,
                    text="Correct: 0     "
                         "Incorrect: 0     "
                         "Accuracy: 100%",
                    font=("Arial", 12))
stats_label.grid(row=3, column=0, pady=10)

def update_stats():
    total = correct_words + incorrect_words
    if total == 0:
        accuracy = 100
    else:
        accuracy = round(correct_words / total * 100)
    stats_label.config(text=f"Correct: {correct_words}     "
                            f"Incorrect: {incorrect_words}     "
                            f"Accuracy: {accuracy}%"
                       )

def countdown():
    global time_remaining, timer_id

    timer_label.config(text=f"Time: {time_remaining}")

    if time_remaining > 0:
        time_remaining -= 1
        timer_id = window.after(1000, countdown)
    else:
        end_test()


def start_timer(event):
    global timer_started
    if not timer_started:
        timer_started = True
        countdown()


def show_results():
    elapsed = 60 - time_remaining

    if elapsed == 0:
        elapsed = 1

    cpm = round(characters_typed * 60 / elapsed)
    ccpm = round(correct_characters * 60 / elapsed)
    wpm = round(ccpm / 5)

    results = Toplevel(window)
    results.title("Results")
    results.geometry("320x250")

    Label(results,
          text="Test Complete",
          font=("Arial", 16, "bold")
          ).pack(pady=10)
    Label(results,
          text=f"Characters/minute : {cpm}"
          ).pack()
    Label(results,
          text=f"Correct characters/minute : {ccpm}"
          ).pack()
    Label(results,
          text=f"Words/minute : {wpm}"
          ).pack()
    Button(results,
           text="Restart",
           command=lambda: restart_test(results)
           ).pack(pady=10)


def restart_test(results_window):
    results_window.destroy()
    window.destroy()
    import os
    os.execl(sys.executable, sys.executable, *sys.argv)

def end_test():
    global timer_id

    if timer_id is not None:
        window.after_cancel(timer_id)

    user_word.config(state="disabled")
    sample_text.config(state="normal")
    sample_text.tag_remove("current", "1.0", END)
    sample_text.config(state="disabled")

    show_results()

user_word.bind("<Key>", start_timer)
user_word.bind("<space>", check_word)
user_word.focus_set()

window.mainloop()