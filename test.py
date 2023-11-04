import pyaudio

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
import detection_emotion_practice as validate
import wave
import pickle
from sys import byteorder
from array import array
from struct import pack
from tkinter.filedialog import askopenfilename
from sklearn.neural_network import MLPClassifier

from utils import extract_feature

root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("test")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('dep1.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Speech Recognition System",font=("Times New Roman", 35, 'bold'),
                    background="black", fg="white", width=60, height=2)
label_l1.place(x=0, y=0)






def upload():
    # load the saved model (after training)
    model = pickle.load(open("mlp_classifier.model", "rb"))
    print("Please talk")
    fileName = askopenfilename(initialdir='/dataset', title='Select image',
                                  filetypes=[("all files", "*.*")])
    filename = fileName    # record the file (start talking)
        #record_to_file(filename)
        # extract features and reshape it
    features = extract_feature(filename, mfcc=True, chroma=True, mel=True,tonnetz=True,contrast=True).reshape(1, -1)
        # predict
    result = model.predict(features)[0]
    result = str(result)
        # show the result !
    print("result:", str(result))
    print(result)
    print(type(result))
    if result == "sad":
        label_l2 = tk.Label(root, text="Person is  Sad",font=("Times New Roman", 20, 'bold'),
                            background="#152238", fg="white", width=30, height=1)
        label_l2.place(x=350, y=200)
    elif result == "happy":
        label_l2 = tk.Label(root, text="Person is  happy",font=("Times New Roman", 20, 'bold'),
                            background="#152238", fg="white", width=30, height=1)
        label_l2.place(x=350, y=200)
    elif result == "neutral":
        label_l2 = tk.Label(root, text="Person is  neutral",font=("Times New Roman", 20, 'bold'),
                            background="#152238", fg="white", width=30, height=1)
        label_l2.place(x=350, y=200)
    elif result == "calm":
        label_l2 = tk.Label(root, text="Person is  calm",font=("Times New Roman", 20, 'bold'),
                            background="#152238", fg="white", width=30, height=1)
        label_l2.place(x=350, y=200)
    elif result == "angry":
        label_l2 = tk.Label(root, text="Person is angry",font=("Times New Roman", 20, 'bold'),
                            background="#152238", fg="white", width=30, height=1)
        label_l2.place(x=350, y=200)
    elif result == "fearful":
        label_l2 = tk.Label(root, text="Person is fearful ",font=("Times New Roman", 20, 'bold'),
                            background="#152238", fg="white", width=30, height=1)
        label_l2.place(x=350, y=200)
    elif result == "disgust":
        label_l2 = tk.Label(root, text="Person is disgust",font=("Times New Roman", 20, 'bold'),
                            background="#152238", fg="white", width=30, height=1)
        label_l2.place(x=350, y=200)
    elif result == "surprised":
        label_l2 = tk.Label(root, text="Person is surprised",font=("Times New Roman", 20, 'bold'),
                            background="#152238", fg="white", width=30, height=1)
        label_l2.place(x=350, y=200)

button1 = tk.Button(root, text="Upload Audio File", command=upload, width=14, height=1,font=('times', 20, ' bold '), bg="purple", fg="white")
button1.place(x=100, y=200)

def window():
  root.destroy()



button2 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button2.place(x=100, y=300)

root.mainloop()    