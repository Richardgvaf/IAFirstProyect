import tkinter as tk
from PIL import ImageTk,Image

class Application(tk.Frame):
    def __init__(self, master=None,Matrix=[]):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x800")
        self.create_board()
        testMatrix = Matrix
        self.show_elements(testMatrix)

    def create_board(self):
        self.matriz = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        icount=0
        jcount=0
        self.image_green = ImageTk.PhotoImage(Image.open("images/green.png"))
        self.image_white = ImageTk.PhotoImage(Image.open("images/white.png"))
        for i in self.matriz:
            for j in i:
                if ((icount+jcount)%2 == 0):
                    self.matriz[icount][jcount] = tk.Label(image=self.image_green)
                else:
                    self.matriz[icount][jcount] = tk.Label(image=self.image_white)
                
                self.matriz[icount][jcount].pack()
                self.matriz[icount][jcount].place(x=jcount*100+100,y=icount*100+100,height=100, width=100)
                jcount +=1
            icount +=1
            jcount = 0

        
    def show_elements(self,show_matrix):
        self.matrix2 = show_matrix;
        icount=0
        jcount=0
        self.image_green_queen = ImageTk.PhotoImage(Image.open("images/green_queen.png"))
        self.image_white_queen = ImageTk.PhotoImage(Image.open("images/white_queen.png"))
        for i in self.matrix2:
            for j in i:
                if (self.matrix2[icount][jcount] == "Q") and ((icount+jcount)%2 == 0):
                    self.matrix2[icount][jcount] = tk.Label(image=self.image_green_queen)
                elif (self.matrix2[icount][jcount] == "Q") and ((icount+jcount)%2 == 1):
                    self.matrix2[icount][jcount] = tk.Label(image=self.image_white_queen)
                elif (icount+jcount)%2 == 0:
                    self.matrix2[icount][jcount] = tk.Label(text=self.matrix2[icount][jcount],image=self.image_green)
                else:
                    self.matrix2[icount][jcount] = tk.Label(text=self.matrix2[icount][jcount],image=self.image_white)
                
                self.matrix2[icount][jcount].pack()
                self.matrix2[icount][jcount].place(x=jcount*100+100,y=icount*100+100,height=100, width=100)
                jcount +=1
            icount +=1
            jcount = 0


    def say_hi(self):
        print("hi there, everyone!")

