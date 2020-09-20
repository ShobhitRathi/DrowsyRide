from tkinter import *
from PIL import ImageTk, Image
import os


def gui_run():
                root = Tk()
                root.configure(background="white")


                def function1(): 
                        os.system("python drowsiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
                        exit()	

                root.title("DROWSYRIDE")

                Label(root, text="DROWSYRIDE", font=("poppins",20),fg="black",bg="white",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)

                
                Button(root,text="Run using web cam",font=("poppins",20),bg="#232733",fg='white',command=function1).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
                Button(root,text="Exit", font=("poppins",20),bg="#232733",fg='white',command=root.destroy).grid(row=9,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

                photo=PhotoImage(file="./static/images/drowsyride.png")

                root.iconphoto(False, photo)
                root.mainloop()
