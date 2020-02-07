#importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

#criando a janela
janela = Tk()
janela.title ("TNT Academia - Login")
janela.geometry ("600x300")
janela.configure (background = "white")
janela.iconbitmap(default ="img/peso.ico")
#não muda o tamanho da janela
janela.resizable (width = False, height = False)
#deixa transparencia na janela
janela.attributes("-alpha",0.9)

#colocando logo
logo = PhotoImage(file="img/icone.png")

#widgets frames direita e esquerda + logo

LeftFrame = Frame(janela,width = 200,height = 300, bg = "red", relief = "raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela,width =395,height = 300, bg = "black", relief = "raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image = logo, bg="red",width=50,height=50)
LogoLabel.place(x=50,y=100)

#titulo
Nome = Label(RightFrame, text = "TNT ACADEMIA", font=("Century Gothic",20),bg="black",fg="red")
Nome.place(x=100,y=30)

#usuario
UserEntry = ttk.Entry(RightFrame,width=40)
UserEntry.place(x=120,y=110)

UserLabel = Label(RightFrame, text = "Usuário:", font=("Century Gothic",20),bg="black",fg="red")
UserLabel.place(x=5,y=100)

#senha
PassEntry = ttk.Entry(RightFrame,width=40,show="*")
PassEntry.place(x=120,y=160)

PassLabel = Label(RightFrame, text = "Senha:", font=("Century Gothic",20),bg="black",fg="red")
PassLabel.place(x=5,y=150)

#função para Login
def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    #irá procurar o usuário e senha no banco de dados
    database.cursor.execute("""
    SELECT * FROM Users
    WHERE (Usuario = ? and Senha = ?)
    """,(User,Pass))
    
    #validação de login
    VerifyLogin = database.cursor.fetchone()
    try:
        if(User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info",message="Acesso Confirmado.Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado.Verifique se está Cadastrado no Sistema.")    


#botões
LoginButton = ttk.Button(RightFrame,text = "Login", width = 20,command = Login)
LoginButton.place(x=145,y=225)


#função para cadastrar novo usuário
def Register():
    #retirando os widgets de login
    LoginButton.place(x=2000)
    RegistroButton.place(x=2000)
    Nome.place(x=2000)
    #colocando widgets de registro
    NomeLabel = Label(RightFrame,text="Nome:",font=("Century Gothic",20),bg="black",fg="red")
    NomeLabel.place(x=5,y=5)

    NomeEntry = ttk.Entry(RightFrame,width = 40)
    NomeEntry.place(x=120,y=20)

    EmailLabel= Label(RightFrame,text="Email:",font=("Century Gothic",20),bg="black",fg="red")
    EmailLabel.place(x=5,y=50)

    EmailEntry = ttk.Entry(RightFrame,width = 40)
    EmailEntry.place(x=120,y=62)


    #função para inserir os dados no banco
    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        Usuario = UserEntry.get()
        Senha = PassEntry.get()

        if(Name == "" or Email == "" or Usuario == "" or Senha == ""):
            messagebox.showerror(title="Erro Registro", message="Preencha Todos os Campos")
        else:    
            database.cursor.execute("""
            INSERT INTO Users (NOME,EMAIL,USUARIO,SENHA) VALUES (?,?,?,?)
            """,(Name,Email,Usuario,Senha))
            #para salvar alterações no banco de dados
            database.conn.commit()
            messagebox.showinfo(title="Registro Info",message="Registrado com Sucesso")

    #botões de registro e voltar
    Register = ttk.Button(RightFrame,text = "Registrar", width = 30,command=RegisterToDataBase)
    Register.place(x=145,y=225)


    #função do botão voltar
    def BacktoLogin():
        #Removendo widgets de cadastro para voltar tela inicial de login
        NomeLabel.place(x=3000)
        NomeEntry.place(x=3000)
        EmailLabel.place(x=3000)
        EmailEntry.place(x=3000)
        Register.place(x=3000)
        Voltar.place(x=3000)
        #Voltando botões de login, registro e titulo
        LoginButton.place(x=145)
        RegistroButton.place(x=145)
        Nome.place(x=100)

    Voltar = ttk.Button(RightFrame,text = "Voltar", width = 30, command = BacktoLogin)
    Voltar.place(x=145,y=260)

RegistroButton = ttk.Button(RightFrame,text = "Registrar", width = 20, command = Register)
RegistroButton.place(x=145,y=260)


janela.mainloop()