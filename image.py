import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cv2 import cv2
root = tk.Tk()
root.title("Operations on Image")
root.geometry("700x300")
root.configure(bg="#98AFC7")
path = tk.StringVar()
l1 = tk.Label(root, text="Choose Image for enhancement",font="arial 20 italic",bg="purple",fg="white").pack()
e1 = tk.Entry(root, width=80, textvariable=path).pack()
# Functions for different operations
def Browse():
    global directory
    directory = tk.filedialog.askopenfilename(initialdir="/", title="Select a file",filetype=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    path.set(directory)
def Original_image():
    plt.imshow(mpimg.imread(directory))
    plt.axis("off")
    plt.show()
def Gray():
    img = cv2.imread(directory, 0)
    plt.imshow(img,cmap='gray',interpolation='bicubic')
    plt.axis("off")
    plt.show()
def Negative():
    img = cv2.imread(directory, 0)
    negative = 255-img
    plt.imshow(negative,cmap='gray',interpolation='bicubic')
    plt.axis("off")
    plt.show()
def Edge_Detect():
    img = cv2.imread(directory, 0)
    edge_image = cv2.Canny(img, 50, 150)
    plt.imshow(edge_image,cmap='gray',interpolation="bicubic")
    plt.axis("off")
    plt.show()
#     Buttons
b1 = tk.Button(root, text="Browse", font="arial 10 bold", bg="red", fg='white', padx=2, command=Browse).pack()
b2 = tk.Button(root, text="Original Image", font = 'arial 10 bold', bg='red', fg="white", padx=2, command=Original_image).place(x=10, y=100)
b3 = tk.Button(root, text="Gray Image", font = 'arial 10 bold', bg='red', fg="white", padx=2, command=Gray).place(x=150, y=100)
b4 = tk.Button(root, text="Negative Image", font = 'arial 10 bold', bg='red', fg="white", padx=2, command=Negative).place(x=290, y=100)
b5 = tk.Button(root, text="Edge Detected Image", font = 'arial 10 bold', bg='red', fg="white", padx=2, command=Edge_Detect).place(x=450, y=100)
root.mainloop()
