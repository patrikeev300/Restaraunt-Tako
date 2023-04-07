import pyodbc
from os import system, name
import os.path
import time
import pathlib
from pathlib import Path
import User
import Order
cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-POTGJ26\SQLEXPRESS;Database=Tako Tako;Trusted_Connection=yes;')
cursor = cnxn.cursor()
ingridientId = []
def CloseOrder(userId, currentIdCheque, endIdDish, count):
    if count == 0:
        User.Users(userId)
    for row in cursor.execute(f"select * from [User] where [ID_User] = {userId}"):
        balance = row.Balance_User
    for row in cursor.execute(f"select * from [Cheque] inner join [User] on [User_ID] = [ID_User] where [ID_Cheque] = {currentIdCheque}"):
        phone = row.Email_User
        count = row.Count_Dish
        cost = row.Cost_Dish
        timeOrder = row.Time_Order
        sum = row.Sum_Order
        ear = row.Ear
        noticed = row.Noticed
    
    for row in cursor.execute(f"select * from [User] inner join [Loyality] on [Loyality_ID] = [ID_Loyality] where [ID_User] = {userId}"):
        loyalityDiscount = row.Discount
        nameLoyality = row.Name_Loyality
    discount = sum * loyalityDiscount
    print(f"Ваша скидка : {discount}")
    balance -= (sum - discount)
    if (balance >= 0):
        cursor.execute(f"update [User] set [Balance_User] = {balance} where [ID_User] = {userId}")
        cnxn.commit()
    else:
        print("Недостаточно денег на счету.")
        time.sleep(2)
        Order.Orders(userId)

    for i in range(len(endIdDish)):
        for row in cursor.execute(f"select * from [Dish_Ingridient] where [Dish_ID] = {endIdDish[i]}"):
            ingridientId.append(row.Ingridient_ID)
    directory = Path(pathlib.Path.cwd(), 'Cheques')
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = Path(pathlib.Path.cwd(), 'Cheques', f'Cheque{currentIdCheque}.txt')
    file = open(directory, 'w')
    file.write(f"Заказ №{currentIdCheque}\n"
               f"Время: {timeOrder}\n"
               f"Пользователь: {phone}\n"
               "\n"
               "Состав заказа: \n"
               "\n"
               f"Токпоки: {count} шт., {cost} руб. за шт.\n"
               "Ингридиенты: \n")
    
    for id in range(len(ingridientId)):
        for row in cursor.execute(f"select * from [Ingridient] where [ID_Ingridient] = {ingridientId[id]}"):
            nameIngridient = row.Name_Ingridient
            costIngridient = row.Cost_Ingridient
            countIngridient = row.Count_Ingridient
        counte = ingridientId.count(ingridientId[id])
        sumIngridient = costIngridient * counte 
        cursor.execute(f"update [Ingridient] set [Count_Ingridient] = {countIngridient - counte} where [ID_Ingridient] = {ingridientId[id]}")
        cnxn.commit()

        file.write(f"{nameIngridient}, {counte} шт., {costIngridient} рублей за шт., {sumIngridient} рублей итого.\n")
               
    file.write(f"Новичок: {ear}\n"
               f"Пользователь заметил: {noticed}\n"
                "\n"
               f"Итого: {sum}")
    file.close()

    print(f"Заказ оформлен! Чек №{currentIdCheque}")
    if (sum > 200):
        cursor.execute(f"update [User] set [Loyality_ID] = 2 where [ID_User] = {userId}")
        cnxn.commit()
    elif (sum > 300):
        cursor.execute(f"update [User] set [Loyality_ID] = 3 where [ID_User] = {userId}")
        cnxn.commit()
    elif (sum > 500):
        cursor.execute(f"update [User] set [Loyality_ID] = 4 where [ID_User] = {userId}")
        cnxn.commit()
    time.sleep(2)
    User.Users(userId)