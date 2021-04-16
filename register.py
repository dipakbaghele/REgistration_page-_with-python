from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("From Registration")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg="black" )


        self.bbg=ImageTk.PhotoImage(file="IMAGES/DTA.jpg")
        bbg=Label(self.root,image=self.bbg).place(x=250, y=0, relwidth=1,relheight=1)

        self.left = ImageTk.PhotoImage(file="IMAGES/D1.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)


        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500 )

        title=Label(frame1, text='Registration Form',font=("new times roman",22,"bold"),bg="blue",fg='white').place(x=50,y=30)

        f_fram=Label(frame1, text='First Name',font=("new times roman",15,"bold"),bg="white",fg='blue').place(x=50,y=100)
        self.text_fname=Entry(frame1,font=("new times roman",15),bg='lightgray')
        self.text_fname.place(x=50,y=130,width=250)

        l_fram = Label(frame1, text='Last Name', font=("new times roman", 15, "bold"), bg="white", fg='blue').place(x=378, y=100)
        self.text_lname = Entry(frame1, font=("new times roman", 15),bg='lightgray')
        self.text_lname.place(x=378, y=130, width=250)

        contact = Label(frame1, text='Contact No', font=("new times roman", 15, "bold"), bg="white", fg='blue').place(x=50, y=170)
        self.text_contact = Entry(frame1, font=("new times roman", 15),bg='lightgray')
        self.text_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text='Email ID', font=("new times roman", 15, "bold"), bg="white", fg='blue').place(x=370, y=170)
        self.text_email = Entry(frame1, font=("new times roman", 15),bg="lightgray")
        self.text_email.place(x=378, y=200 , width=250)

        question= Label(frame1, text='Sequrity question:', font=("new times roman", 15, "bold"), bg="white", fg='blue').place(x=50,y=260)
        self.cmd_question = ttk.Combobox(frame1, font=("new times roman", 13))
        self.cmd_question['value']=('select','your best friend','your best sport',)
        self.cmd_question.current(0)
        self.cmd_question.place(x=50, y=300, width=250)

        answer = Label(frame1, text='Answer', font=("new times roman", 15, "bold"), bg="white", fg='blue').place(x=370,y=260)
        self.text_answer = Entry(frame1, font=("new times roman", 15), bg='lightgray')
        self.text_answer.place(x=370, y=300, width=250)

        password = Label(frame1, text='Password', font=("new times roman", 15, "bold"), bg="white", fg='blue').place(x=50,
                                                                                                                  y=350)
        self.text_password = Entry(frame1, font=("new times roman", 15), bg='lightgray')
        self.text_password.place(x=50, y=390, width=250)

        cpass =Label(frame1, text='Conform Password', font=("new times roman", 15, "bold"), bg="white", fg='blue').place(
            x=370, y=350)
        self.text_cpass = Entry(frame1, font=("new times roman", 15), bg='lightgray')
        self.text_cpass.place(x=370, y=390, width=250)

        self.reg= Button(frame1, bd=5, text='Register', font=("new times roman", 20), cursor="hand2",bg="black" ,fg='yellow',command=self.register_d).place(
        x=50, y=430)

        btn_login=Button(self.root,bd=7,text='sign In',font=('time new roman',20),bg='black',fg='yellow').place(x=180,y=480)

    def register_d(self, mysql=None):
        if self.text_fname.get()=="" or self.text_lname.get()=="" or self.text_contact.get()=="select"or self.text_email.get()=="" or self.cmd_question.get()=="" or self.text_answer.get() == "" or self.text_password.get()==""  or self.text_cpass.get()=="" :
            messagebox.showerror("warning","All field are required to fill ",parent=self.root)

        elif self.text_password.get() != self.text_cpass.get():
            messagebox.showerror("waring","password & conform password should  be same",parent=self.root )

        else:
            try:
                con=mysql.connect(host="localhost",user="root",password="",db="registerdb")
                cur=con.cursor()
                cur.execution("inser into login_register(f_name,l_name,contact,email,question,answer,password)value(%s,%s,%s,%s,%s,%s,%s,)",
                              (
                                  self.text_fname.get(),
                                  self.text_lname.get(),
                                  self.text_contact.get(),
                                  self.text_email.get(),
                                  self.cmd_question.get(),
                                  self.text_answer.get(),
                                  self.text_password.get(),

                                
                              ))
                con.commit()
                con.close()
                messagebox.showinfo("success","Register Succesffully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error","error handle,{str(es)}",parent=self.root)



root=Tk()
obj=Register(root)
root.mainloop()

