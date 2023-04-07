import pyodbc
from os import system, name
import time
import random
cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-POTGJ26\SQLEXPRESS;Database=Tako Tako;Trusted_Connection=yes;')
cursor = cnxn.cursor()

def Regss(email, password):
    _ = system('cls')
    print("Ошибка")
    loyality = 1
    confirmReg = True
    role = 2
    email_user = []
    for row in cursor.execute("select * from [User]"):
        email_user.append(row.Email_User)

    for id in range(len(email_user)):
        if email == email_user[id]:
            confirmReg = False
    
    if confirmReg == True:
        random.seed()
        balance = random.randint(1000, 10000)
        cursor.execute("insert into [User] ([Loyality_ID], [Email_User], [Password_User], [Role_ID], [Balance_User]) values (?, ?, ?, ?, ?)", 
                       loyality, email, password, role, balance)
        cnxn.commit()
        time.sleep(2)
        print("Аккаунт зарегистрирован.")
        time.sleep(2)
        #Main.mainwindow()
    else:
        print("Такой номер телефона уже зарегистрирован")
        time.sleep(2)
        #Main.mainwindow()