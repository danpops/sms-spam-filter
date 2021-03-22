# IMPORTS
from dearpygui.core import *
from dearpygui.simple import *

# SMS SPAM FILTER IMPORTS
import random
import pandas as pd
import string
import nltk

# functions.py IMPORTS
from functions import categorize_words, pre_process, predict

nltk.download('punkt')
nltk.download('stopwords')


# BUTTON CALLBACK FUNCTION
# RUN EACH TIME WHEN THE "Check" BUTTON IS CLICKED
def check_spam(sender, caller, pred=None):
    if pred is None:
        pred = []
    with window("Simple SMS Spam Filter"):
        if not pred:
            # RUNS ONLY ONCE WHEN BUTTON IS FIRST CLICKED
            # AND WHEN pred[-1] WIDGET DOESN'T EXIST
            add_spacing(count=12)
            add_separator()
            add_spacing(count=12)
        else:
            # HIDE PREDICTION WIDGET
            hide_item(pred[-1])

        # COLLECT INPUT, PRE-PROCESS AND GET PREDICTION
        input_value = get_value("Input")
        input_value = pre_process(input_value)
        pred_text, text_colour = predict(input_value)

        # STORE PREDICTION INSIDE THE PRED LIST
        pred.append(pred_text)
        # DISPLAY PREDICTION TO USER
        add_text(pred[-1], color=text_colour)


# WINDOW OBJECT SETTINGS
set_main_window_size(520, 750)
set_global_font_scale(1.00)
set_theme("Blue")
set_style_window_padding(30, 30)

with window("Simple SMS Spam Filter", width=520, height=800):
    print("GUI is running...")
    set_window_pos("Simple SMS Spam Filter", 0, 0)

    # LOGO
    add_drawing("logo", width=520, height=290)
    add_separator()
    add_spacing(count=12)

    # INSTRUCTIONS
    add_text("Please enter an SMS message of your choice to check if it's spam or not.",
             wrap=500,
             color=[30, 144, 255])
    add_spacing(count=12)

    # COLLECT INPUT
    add_input_text("Input", width=415, default_value="type message here!")
    add_spacing(count=12)
    add_button("Check", callback=check_spam)

# PLACE IMAGE INSIDE THE SPACE
draw_image("logo", "logo_spamFilter.png", [0, 0], [458, 192])

start_dearpygui()
print("Exiting GUI")
