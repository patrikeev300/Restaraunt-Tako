import pyodbc
from os import system, name
import os.path
import time
import Order
import random
import datetime
now = datetime.datetime.now()
cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-POTGJ26\SQLEXPRESS;Database=Tako Tako;Trusted_Connection=yes;')
cursor = cnxn.cursor()

def ChequeSumUpd(userId, currentIdCheque, endIdDish):
    ingridientId = []
    sum = 0
    for row in cursor.execute(f"select * from [Cheque] inner join [User] on [User_ID] = [ID_User] where [ID_Cheque] = {currentIdCheque}"):
        count = row.Count_Dish
        cost = row.Cost_Dish
        sum = row.Sum_Order
    sum = 0
    sum += cost * count 
    ingridientId = []
    for i in range(len(endIdDish)):
        for row in cursor.execute(f"select * from [Dish_Ingridient] where [Dish_ID] = {endIdDish[i]}"):
            ingridientId.append(row.Ingridient_ID)
    
    for id in range(len(ingridientId)):
        for row in cursor.execute(f"select * from [Ingridient] where [ID_Ingridient] = {ingridientId[id]}"):
            costIngridient = row.Cost_Ingridient
        sum += costIngridient

    cursor.execute(f"update [Cheque] set [Sum_Order] = {sum} where [ID_Cheque] = {currentIdCheque}")
    cnxn.commit()


def Cheque(userId, count):
    for row in cursor.execute("select * from [Dish]"):
        cost = row.Cost_Dish
        
    sum = count * cost
    currentTime = now.strftime("%d-%m-%Y %H:%M")
    random.seed()
    if random.randint(1, 10) > 5:
        ear = True
        random.seed()
        if random.randint(1, 10) > 5:
            detected = True
        else:
            detected = False
    else:
        ear = False
        detected = False
    
    cursor.execute("insert into [Cheque] ([User_ID], [Count_Dish], [Cost_Dish], [Sum_Order], [Time_Order], [Ear], [Noticed]) values (?, ?, ?, ?, ?, ?, ?)", 
                   (userId, count, cost, sum, currentTime, (1 if ear else 0), (1 if detected else 0)))
    cnxn.commit()

def DropCheque(userId, currentIdCheque):
    Dishes = []
    for row in cursor.execute(f"select * from [Cheque_Dish] where [Cheque_ID] = {currentIdCheque}"):
        Dishes.append(row.Dish_ID)
    for id in range(len(Dishes)):
        cursor.execute(f"delete [Dish] where [ID_Dish] = {Dishes[id]}")
        cnxn.commit()
    cursor.execute(f"delete [Cheque] where [ID_Cheque] = {currentIdCheque}")
    cnxn.commit()
    
    print("Возвращаемся в главное меню...")
    time.sleep(2)
    Order.Order(userId)