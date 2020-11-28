from tkinter import *
import time
from Logic import mainApp

class GUI():

    def __init__(self):
        self.canvas = None
        self.frame = None
        self.last_ccp = ""
        self.the_while_bool = False
        self.all_links = []
        self.btn_720 = None
        self.root = Tk()
        self.root.geometry("600x600")
        self.canva()
        self.the_frame()
        self.Show_Links()
        self.Buttons_Entry()
        self.root.mainloop()

    def canva(self):

        self.canvas = Canvas(self.root,height=600,width=600)
        self.canvas.pack()
    def the_frame(self):
        fileFrame = Frame(self.root,bg="white")
        fileFrame.place(relwidth=0.8,relheight=0.6,relx=0.1,rely=0.1)
        self.frame = fileFrame

    def Show_Links(self,clear=False):

        if clear==True:
            self.all_links = []
        for widget in self.frame.winfo_children():
            widget.destroy()
        if self.all_links != []:
            for link in self.all_links : 
                label = Label(self.frame,text=link,bg="Pink")
                label.pack()

    def Buttons_Entry(self):
        self.btn_720 = Button(self.canvas,text=720,height=5,width=10,command=lambda:self.Quality(720))
        self.btn_720.grid(row=2,column=1)
        self.btn_480 = Button(self.canvas,text=480,height=5,width=10,command=lambda:self.Quality(480))
        self.btn_480.grid(row=2,column=2)

        self.btn_360 = Button(self.canvas,text=360,height=5,width=10,command=lambda:self.Quality(360))
        self.btn_360.grid(row=2,column=3)

        self.add = Button(self.root,text="Add",height=5,width=10,command=lambda:self.Add_Link(self.entry.get()))
        self.add.place(relwidth=0.1,relheight=0.1,relx=0.6,rely=0.7)
        self.entry = Entry(self.root)
        self.entry.place(relwidth=0.5,relheight=0.1,relx=0.1,rely=0.7)
        self.clear = Button(self.root,text="clear",height=5,width=10,command=lambda:self.Show_Links(True))
        self.clear.place(relwidth=0.1,relheight=0.1,relx=0.7,rely=0.7)
        self.ram = Button(self.root,text="RAM",height=5,width=10,command=lambda:self.the_while())
        self.ram.place(relwidth=0.1,relheight=0.1,relx=0.8,rely=0.7)
        self.run = Button(self.root,text="RUN !!",height=5,width=10,command=lambda:self.Run())
        self.run.place(relwidth=0.8,relheight=0.1,relx=0.1,rely=0.9)


    def Quality(self,q):
        
        if q == 720:

            self.btn_720 = Button(self.canvas,text=720,height=5,width=10,bg="Green",command=lambda:self.Quality(720))
            self.btn_720.grid(row=0,column=1)

            self.btn_480 = Button(self.canvas,text=480,height=5,width=10,command=lambda:self.Quality(480))
            self.btn_480.grid(row=0,column=2)
            self.btn_360 = Button(self.canvas,text=360,height=5,width=10,command=lambda:self.Quality(360))
            self.btn_360.grid(row=0,column=3)
        if q == 480:

            self.btn_720 = Button(self.canvas,text=720,height=5,width=10,command=lambda:self.Quality(720))
            self.btn_720.grid(row=0,column=1)

            self.btn_480 = Button(self.canvas,text=480,height=5,width=10,bg="Green",command=lambda:self.Quality(480))
            self.btn_480.grid(row=0,column=2)

            self.btn_360 = Button(self.canvas,text=360,height=5,width=10,command=lambda:self.Quality(360))
            self.btn_360.grid(row=0,column=3)

            

        if q == 360:

            self.btn_720 = Button(self.canvas,text=720,height=5,width=10,command=lambda:self.Quality(720))
            self.btn_720.grid(row=0,column=1)

            self.btn_480 = Button(self.canvas,text=480,height=5,width=10,command=lambda:self.Quality(480))
            self.btn_480.grid(row=0,column=2)

            self.btn_360 = Button(self.canvas,text=360,height=5,width=10,bg="Green",command=lambda:self.Quality(360))
            self.btn_360.grid(row=0,column=3)


        self.quality = q
        print(self.quality)
    
    def Add_Link(self,link):

        self.all_links.append(link)
        self.entry.delete(0,END)
        self.Show_Links()
        self.last_ccp = link

    def from_RAM(self):
        
        last_in_clip = self.root.clipboard_get()
        if last_in_clip !=self.last_ccp :
            self.Add_Link(last_in_clip)
            self.last_ccp = last_in_clip


    def the_while(self):
        self.root.clipboard_clear()
        self.the_while_bool = not self.the_while_bool
        while self.the_while_bool:
            time.sleep(1)
            if self.the_while_bool == False:
                break
            else:
                self.from_RAM()
                

    def Run(self):

        r = mainApp(self.quality,self.all_links)


x = GUI()














