import pyodbc
from os import system, name
import Admin
import User
import time
cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-POTGJ26\SQLEXPRESS;Database=Tako Tako;Trusted_Connection=yes;')
cursor = cnxn.cursor()
def Auth(email, password):
    _ = system('cls')
    
    isAuthorized = False
    email_user, pass_user, email_admin, pass_admin = [], [], [], []
    for row in cursor.execute("select * from [User] where [Role_ID] = 2"):
        email_user.append(row.Email_User)
        pass_user.append(row.Password_User)
    
    for row in cursor.execute("select * from [User] where [Role_ID] = 1"):
        email_admin.append(row.Email_User)
        pass_admin.append(row.Password_User)
    
    for id in range(len(email_admin)):
        if email == email_admin[id] and password == pass_admin[id]:
            for row in cursor.execute(f"select * from [User] where [Role_ID] = 1 and [Email_User] = '{email}' "):
                adminId = row.ID_User
            isAuthorized = True
            Admin.Admin(adminId)
    for id in range(len(email_user)):
        if email == email_user[id] and password == pass_user[id]:
            for row in cursor.execute(f"select * from [User] where [Role_ID] = 2 and [Email_User] = '{email}' "):
                userId = row.ID_User
            isAuthorized = True
            User.Users(userId)
    if isAuthorized == False:
        print("Неправильно введенные данные")
        time.sleep(2)
        exit()