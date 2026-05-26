from tkinter import *
from mydb import DataBase
from tkinter import messagebox
from myapi import API
import sys
class NLPApp:
    def __init__(self):
       
        #create db object
        self.dbo=DataBase()
        #create api obj
        self.apio=API()
        self.root=Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')
        self.login_gui()
        self.root.mainloop()
 
    def login_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))
        
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)
        
        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))
        
        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)
        
        login_btn=Button(self.root,text='Login',width=20,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))
        
        label3=Label(self.root,text='Not a member ?')
        label3.pack(pady=(20,10)) 

        redirect_btn=Button(self.root,text='Register Now',command=self.register_gui)
        redirect_btn.pack(pady=(10,10))
    
    def register_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        
        label0=Label(self.root,text='Enter Name')
        label0.pack(pady=(10,10))
        
        self.name_input=Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)
        
        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))
        
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)
        
        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))
        
        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)
        
        register_btn=Button(self.root,text='register',width=20,height=2,command=self.perform_registeration)
        register_btn.pack(pady=(10,10))
        
        label3=Label(self.root,text='Already a member ?')
        label3.pack(pady=(20,10)) 

        redirect_btn=Button(self.root,text='Login Now',command=self.login_gui)
        redirect_btn.pack(pady=(10,10))
        
    def perform_registeration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        
        response=self.dbo.add_data(email,name,password)
        if response:
            messagebox.showinfo('Success','Registration successful. You can login now')
        else :
            messagebox.showerror('Error','Email already exists')
            
    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()
        response=self.dbo.search(email,password)
        if response:
            messagebox.showinfo('success','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect email/password')
    def home_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))
            
        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=30,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))  
        
        ner_btn=Button(self.root,text='Named Entity Recognition',width=30,height=4,command=self.ner_gui)
        ner_btn.pack(pady=(10,10))  
        
        emotion_btn=Button(self.root,text='Emotion Detection',width=30,height=4,command=self.emotion_gui)
        emotion_btn.pack(pady=(10,10))    

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))
    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))
        
        heading2 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))
        
        label1=Label(self.root,text='Enter text')
        label1.pack(pady=(10,10))
        
        self.sentiment_input=Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=4)

    
        sentiment_btn = Button(self.root, text='Analyze sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))
        
        self.sentiment_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana',16))
        

        
        goback_btn=Button(self.root,text="Go Back",command=self.home_gui)
        goback_btn.pack(pady=(10,10))
        
    def do_sentiment_analysis(self):
        response=self.apio.sentiment_analyze(self.sentiment_input.get())
        txt=""
        for item in response:
            emotion=item.label
            percentage=round(item.score*100,2)
            txt+="{} : {}%\n".format(emotion,percentage)
        print(txt)   
        self.sentiment_result.configure(text=txt)
        messagebox.showinfo('Sentiment analysis successfull')
        
    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))
        
        heading2 = Label(self.root, text='Named Entity Recognition', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))
        
        label1=Label(self.root,text='Enter Text')
        label1.pack(pady=(10,10))
        
        self.ner_input=Entry(self.root,width=50)
        self.ner_input.pack(pady=(5,10),ipady=4)

    
        ner_btn = Button(self.root, text='Do NER', command=self.do_ner)
        ner_btn.pack(pady=(10, 10))
        
        self.ner_result = Label(self.root, text='',bg='#34495E',fg='white',wraplength=300)
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana',16))
        
        goback_btn=Button(self.root,text="Go Back",command=self.home_gui)
        goback_btn.pack(pady=(10,10))
    def do_ner(self):
        response=self.apio.recognize_entities(self.ner_input.get())
        txt=""
        for item in response:
            entity_type=item.entity_group
            word=item.word
            confidence=round(item.score*100,1)
            txt+="[{}] {} ({}%)\n".format(entity_type,word,confidence)
        print(txt)
        self.ner_result.configure(text=txt)
    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))
        
        heading2 = Label(self.root, text='Emotion Detection', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))
        
        label1=Label(self.root,text='Enter Text')
        label1.pack(pady=(10,10))
        
        self.emotion_input=Entry(self.root,width=50)
        self.emotion_input.pack(pady=(5,10),ipady=4)

    
        emotion_btn = Button(self.root, text='Predict Emotion', command=self.do_emotion_prediction)
        emotion_btn.pack(pady=(10, 10))
        
        self.emotion_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('verdana',16))
        
        goback_btn=Button(self.root,text="Go Back",command=self.home_gui)
        goback_btn.pack(pady=(10,10))
        
    def do_emotion_prediction(self):
        response=self.apio.predict_emotion(self.emotion_input.get())
        txt=""
        for item in response:
            emotion=item.label.capitalize()
            percentage=round(item.score*100,2)
            txt+="{} : {}%\n".format(emotion,percentage)  
        print(txt)         
        self.emotion_result.configure(text=txt)
        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
nlp=NLPApp()
    
   


# database structure json
# {
# email:[name,pass],
# email:[name,pass],
# ....
# }
