from tkinter import *
from My_Database import Database
from tkinter import messagebox 
from API_key import API
import json



class NLPapp:
     



    def __init__(self):

        # Create a Database object
        self.db = Database()
        self.API = API()

        self.root = Tk()
        self.root.title('TextSense')
        self.root.iconbitmap(r'D:\NLP app (GUI)\favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg = '#566573')

        self.login_page()

        self.root.mainloop()



    def login_page(self):
        self.clear()

        heading = Label(self.root,text ='TextSense',bg = '#566573',fg = 'white')
        heading.pack(pady = (20,30))
        heading.configure(font = ('Verdana',24,'bold'))

        Email = Label(self.root,text = 'Email',font = ('Calibri',11))
        Email.pack(pady = (10,10))

        self.Email_box = Entry(self.root, width = 40)
        self.Email_box.pack(pady = (5,10), ipady = 3)

        Password = Label(self.root,text = 'Password',font = ('Calibri',11))
        Password.pack(pady = (10,10))

        self.password_box = Entry(self.root, width = 40,show = '*')
        self.password_box.pack(pady = (5,10), ipady = 3)

        Login_Button = Button(self.root,text = 'Login',font = ('Calibri',11),width = 10 ,height = 1,command = self.perform_login)
        Login_Button.pack(pady = (30,10))

        Not_member = Label(self.root,text = 'New user create account?',font = ('Calibri',14,'bold'),bg = '#566573',fg = 'white')
        Not_member.pack(pady = (50,10))

        Register_Button = Button(self.root,text = 'Register',font = ('Calibri',11),width = 9, height = 1,command = self.Register_GUI )
        Register_Button.pack(pady = (10,10))
    




    def Register_GUI(self):
        self.clear()

        heading = Label(self.root,text ='TextSense',bg = '#566573',fg = 'white')
        heading.pack(pady = (20,30))
        heading.configure(font = ('Verdana',24,'bold'))

        First_Name = Label(self.root,text = 'First Name',font = ('Calibri',11))
        First_Name.pack(pady = (10,10))

        self.First_Name_box = Entry(self.root, width = 40)
        self.First_Name_box.pack(pady = (5,10), ipady = 3)

        Last_Name = Label(self.root,text = 'Last Name',font = ('Calibri',11))
        Last_Name.pack(pady = (10,10))

        self.Last_Name_box = Entry(self.root, width = 40)
        self.Last_Name_box.pack(pady = (5,10), ipady = 3)

        Email = Label(self.root,text = 'Email',font = ('Calibri',11))
        Email.pack(pady = (10,10))

        self.Email_box = Entry(self.root, width = 40)
        self.Email_box.pack(pady = (5,10), ipady = 3)

        Password = Label(self.root,text = 'Password',font = ('Calibri',11))
        Password.pack(pady = (10,10))

        self.password_box = Entry(self.root, width = 40,show = '*')
        self.password_box.pack(pady = (5,10), ipady = 3)

        Register_Button = Button(self.root,text = 'Register',font = ('Calibri',11),width = 10 ,height = 1,command = self.Perform_registration)
        Register_Button.pack(pady = (30,10))

        Already_member = Label(self.root, text = 'Already user account?',font = ('Calibri',14,'bold'),bg = '#566573',fg = 'white')
        Already_member.pack(pady = (10,10))

        Login_Button = Button(self.root,text = 'Login',font = ('Calibri',11),width = 9, height = 1,command = self.login_page )
        Login_Button.pack(pady = (10,10))





    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()




    def Perform_registration(self):
        # Fetch data from GUI 
        First_name = self.First_Name_box.get()
        Last_name = self.Last_Name_box.get()
        Email = self.Email_box.get()
        Password = self.password_box.get()
        
        Response = self.db.Add_data(First_name,Last_name,Email,Password)

        if Response:
            messagebox.showinfo('Great','Registration successfull')
        else:
            messagebox.showerror('Error','User already exists')




    def perform_login(self):
        Email = self.Email_box.get()
        Password = self.password_box.get()

        Response = self.db.Search(Email, Password)

        if Response:
            messagebox.showinfo('Great','Login successfull')
            self.Home_page()
        else:
            messagebox.showerror('Error','Incorrect Email/Password')

    


    def Home_page(self):

        self.clear()

        heading = Label(self.root,text ='TextSense',bg = '#566573',fg = 'white')
        heading.pack(pady = (20,30))
        heading.configure(font = ('Verdana',24,'bold'))


        Sentiment_Button = Button(self.root,text = 'Sentiment analysis',font = ('Calibri',11),width = 30 ,height = 4,command = self.Perform_sentiment)
        Sentiment_Button.pack(pady = (10,10))

        NameEntity_Button = Button(self.root,text = 'Name Entity recognition',font = ('Calibri',11),width = 30 ,height = 4,command = self.Perform_Name_Entity_Recognition)
        NameEntity_Button.pack(pady = (10,10))

        Emotion_Button = Button(self.root,text = 'Emotion prediction',font = ('Calibri',11),width = 30 ,height = 4,command = self.Perform_Emotion_prediction)
        Emotion_Button.pack(pady = (10,10))

        Logout_Button = Button(self.root,text = 'Logout',font = ('Calibri',11),width = 9, height = 1,command = self.login_page)
        Logout_Button.pack(pady = (20,10))




    def Perform_sentiment(self):

        self.clear()

        heading = Label(self.root,text ='TextSense',bg = '#566573',fg = 'white')
        heading.pack(pady = (20,30))
        heading.configure(font = ('Verdana',24,'bold'))

        sentiment_heading = Label(self.root,text ='Sentiment analysis',bg = '#566573',fg = 'white')
        sentiment_heading.pack(pady = (10,30))
        sentiment_heading.configure(font = ('Verdana',20))

        Enter_text = Label(self.root,text = 'Enter text/paragraph',font = ('Calibri',11))
        Enter_text.pack(pady = (10,10))

        self.sentiment_text = Entry(self.root,width = 50)
        self.sentiment_text.pack(pady = (10,10),ipady = 4)

        Sentimentanalyze_Button = Button(self.root,text = 'Analyze',font = ('Calibri',11),width = 9, height = 1,
            command = self.sentiment_result )
        Sentimentanalyze_Button.pack(pady = (10,10))

        self.Sentimentresult = Label(self.root,text = '',bg = '#566573',fg = 'white')
        self.Sentimentresult.pack(pady = (10,10))
        self.Sentimentresult.configure(font = ('verdana',12))

        Goback_Button = Button(self.root,text = 'Back',font = ('Calibri',11),width = 11, height = 1,command = self.Home_page)
        Goback_Button.pack(pady = (40,10))




    def sentiment_result(self):

        text = self.sentiment_text.get()
        Result = self.API.sentiment_analysis_result(text)

        E = ''
        for i in Result:
            l = i[0]
            s = i[1]
            E = f'{i[0]} \n {i[1]}'
        print(E)
        self.Sentimentresult['text'] = E




    def Perform_Name_Entity_Recognition(self):

        self.clear()

        heading = Label(self.root,text ='TextSense',bg = '#566573',fg = 'white')
        heading.pack(pady = (20,30))
        heading.configure(font = ('Verdana',24,'bold'))

        Name_Entity_heading = Label(self.root,text ='Name Entity Recognition',bg = '#566573',fg = 'white')
        Name_Entity_heading.pack(pady = (10,30))
        Name_Entity_heading.configure(font = ('Verdana',20))

        Enter_text = Label(self.root,text = 'Enter text/paragraph',font = ('Calibri',11))
        Enter_text.pack(pady = (10,10))

        self.Name_Entity_text = Entry(self.root,width = 50)
        self.Name_Entity_text.pack(pady = (10,10),ipady = 4)

        Name_Entity_Button = Button(self.root,text = 'Analyze',font = ('Calibri',11),width = 9, height = 1,
            command = self.Name_Entity_result )
        Name_Entity_Button.pack(pady = (10,10))

        self.NameEntityresult = Label(self.root,text = '',bg = '#566573',fg = 'white')
        self.NameEntityresult.pack(pady = (10,10))
        self.NameEntityresult.configure(font = ('verdana',12))

        Goback_Button = Button(self.root,text = 'Back',font = ('Calibri',11),width = 11, height = 1,command = self.Home_page)
        Goback_Button.pack(pady = (40,10))




    def Name_Entity_result(self):

        text = self.Name_Entity_text.get()
        
        try:
            Result = self.API.NER_result(text)

            f = '\n'.join(map(str,Result))

            self.NameEntityresult.config(text = f)
        except Exception as e:
            self.NameEntityresult.config(text = 'Error processing request')
            print(e)





    def Perform_Emotion_prediction(self):

        self.clear()

        heading = Label(self.root,text ='TextSense',bg = '#566573',fg = 'white')
        heading.pack(pady = (20,30))
        heading.configure(font = ('Verdana',24,'bold'))

        Emotion_heading = Label(self.root,text ='Emotion prediction',bg = '#566573',fg = 'white')
        Emotion_heading.pack(pady = (10,30))
        Emotion_heading.configure(font = ('Verdana',20))

        Enter_text = Label(self.root,text = 'Enter text/paragraph',font = ('Calibri',11))
        Enter_text.pack(pady = (10,10))

        self.Emotion_text = Entry(self.root,width = 50)
        self.Emotion_text.pack(pady = (10,10),ipady = 4)

        Emotion_Button = Button(self.root,text = 'Analyze',font = ('Calibri',11),width = 9, height = 1,
            command = self.Emotion_prediction_result)
        Emotion_Button.pack(pady = (10,10))

        self.Emotionresult = Label(self.root,text = '',bg = '#566573',fg = 'white')
        self.Emotionresult.pack(pady = (10,10))
        self.Emotionresult.configure(font = ('verdana',12))

        Goback_Button = Button(self.root,text = 'Back',font = ('Calibri',11),width = 11, height = 1,command = self.Home_page)
        Goback_Button.pack(pady = (40,10))




    def Emotion_prediction_result(self):
        text = self.Emotion_text.get()
        
        try:
        
            Result = self.API.Emotion_result(text)
        

            o = ''
            for i in Result[0]:
                label = i.get('label')
                score = i.get('score')
                o += f"{label.capitalize()} : {score:.2f}\n"        
        
            self.Emotionresult.config(text = o.strip())

        except Exception as e:
            self.Emotionresult.config(text = 'Error processing request')
            print(e)


nlp = NLPapp()