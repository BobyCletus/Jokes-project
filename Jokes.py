

# Boby Cletus
# 10526525


import tkinter
import tkinter.messagebox
import json

class ProgramGUI:

        # class constructor for ProgramGUI
    
    def __init__(self):

        # tkinter main window set up
        self.main = tkinter.Tk()
        self.main.title('Jokes Catelogue')
        self.main.geometry('400x180')
        self.main.resizable(width=True,height=False)
        self.main.attributes('-alpha', 1)
        self.main.attributes('-topmost', True)

        # reading the data from the text file
        
        try:

            f = open('data.txt','r')   
            self.data = json.load(f)
            f.close()

        except:
            tkinter.messagebox.showerror('Missing/invalid file')
            self.main.destroy()
          
        
        self.current_joke = 0

        # set up Frames
        self.setup = tkinter.Frame(self.main, padx=8, pady=4)
        self.choice = tkinter.Frame(self.main, padx=8, pady=4)


        # setup and pack Labels to show jokes
        self.setupJoke = tkinter.Label(self.setup, width=30, justify='center')
        self.setupJoke.pack(side='top')

        self.punchJoke = tkinter.Label(self.setup, width=30, justify='center')
        self.punchJoke.pack(side='top')


        # setup and pack rating buttons
        self.laughButt = tkinter.Button(self.choice,width=8,padx=4,pady=4,fg='blue', text='Laugh', command= lambda: self.rate_joke('laughs'))
        self.laughButt.pack(side='left')
        self.groanButt = tkinter.Button(self.choice, width =8,padx=4,pady=4,fg='blue',text='Groan', command= lambda: self.rate_joke('groans'))
        self.groanButt.pack(side='left')

        #pack Frame widgets
        self.setup.pack()
        self.choice.pack(side= 'bottom')
        # call show joke method for displaying set up and punchline of the first joke.
        self.show_joke()
        tkinter.mainloop()

    

    def show_joke(self):
        
        self.data[0] = self.data[self.current_joke]
        self.setupJoke.configure(text =self.data[0]['setup'])
        self.punchJoke.configure(text = self.data[0]['punchline'])
        

       # create function for recording the rating of the joke.
    
    def rate_joke(self, rating):
        self.data[self.current_joke][rating]+=1

        # update joke data dict and write the self.data list to JSON format.
        f = open('data.txt','w')
        json.dump(self.data,f)
        f.close()

        try:
            if len (self.data) ==1 :
                tkinter.messagebox.showinfo('Thank you for rating. That was the last joke. The program will now end.')

            else:
                tkinter.messagebox.showinfo('Thank you for rating. The next joke will now appear.')
                self.current_joke = self.current_joke+1
                self.show_joke()

                
        except IndexError:
            tkinter.messagebox.showerror('The End')
            self.main.destroy()
                      
            
        
gui = ProgramGUI()


    























        
