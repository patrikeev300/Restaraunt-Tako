set quoted_identifier on
go
set ansi_nulls on
go

create database [Tako Tako]
go
use [Tako Tako]
go

create table [dbo].[Dish]
(
  [ID_Dish] [int] not null identity(1,1),
  [Cost_Dish] [int] not null
  constraint [PK_Dish] primary key clustered 
  ([ID_Dish] ASC) on [PRIMARY]
)
go

insert into [dbo].[Dish]([Cost_Dish])
values (279)



create table [dbo].[Role]
(
  [ID_Role] [int] not null identity(1,1),
  [Name_Role] [varchar] (30) not null,
  constraint [PK_Role] primary key clustered 
  ([ID_Role] ASC) on [PRIMARY]
)
go
insert into [dbo].[Role]([Name_Role])
values ('Админ'),
('Пользователь')
go

create table [dbo].[Type_Ingridient]
(
  [ID_Type] [int] not null identity(1,1),
  [Name_Type] [varchar] (30) not null,
  constraint [PK_Type] primary key clustered 
  ([ID_Type] ASC) on [PRIMARY]
)
go
insert into [dbo].[Type_Ingridient]([Name_Type])
values ('Зелень'),
('Курицы'),
('Морковь'),
('бекон'),
('соус'),
('яйца')
go

select * from [Type_Ingridient]
go

create table [Loyality]
(
	[ID_Loyality] [int] not null identity(1,1) primary key,
	[Name_Loyality] [VARCHAR] (50) not null unique,
	[Discount] [float] not null
)
go

insert into [Loyality] ([Name_Loyality], [Discount]) values
('None', 0),
('Bronze', 0.15),
('Silver', 0.25),
('Gold', 0.35)
go

select * from [Loyality]
go

create table [User]
(
	[ID_User] [int] not null identity(1,1) primary key,
	[Loyality_ID] [int] not null references [Loyality] (ID_Loyality) on delete cascade,
	[Email_User] [VARCHAR](200) not null unique check ([Email_User] like ('%@%.%')),
	[Password_User] [VARCHAR](50) not null,
	[Role_ID] [int] not null,
	[Balance_User] [int] not null default(10000)
	constraint [FK_Role_User] foreign key ([Role_ID])
	references [dbo].[Role] ([ID_Role])
)
go

insert into [User] ([Loyality_ID], [Email_User], [Password_User], [Role_ID], [Balance_User]) values
(1, 'patrikeevwork@gmail.com', '1234', 1, 10000),
(1, 'patrikeev100@bk.ru', '1234', 2, 10000)
go

select * from [User]
go

create table [dbo].[Ingridient]
(
  [ID_Ingridient] [int] not null identity(1,1),
  [Name_Ingridient] [varchar] (30) not null,
  [Cost_Ingridient] [int]  null,
  [Count_Ingridient] [int] not null,
  [Type_ID] [int]  null,
  constraint [FK_Type_Ingridient] foreign key ([Type_ID])
  references [dbo].[Type_Ingridient] ([ID_Type]),
  constraint [PK_Ingridient] primary key clustered 
  ([ID_Ingridient] ASC) on [PRIMARY]
)
go
insert into [dbo].[Ingridient]([Name_Ingridient], [Cost_Ingridient], [Count_Ingridient], [Type_ID])
values ('Руколла', 10, 100, 1),
('Салат', 10, 100, 1),
('Печеная', 10, 100, 2),
('Вареная', 30, 100, 2),
('Жареная', 30, 100, 2),
('По-корейски', 30, 100, 3),
('Вареная', 25, 100, 3),
('Фаршированная', 20, 100, 3),
('Кенза', 15, 100, 1), 
('Жаренный', 10, 100, 4),
('Сырный', 15, 100, 4),
('Варено-копченый', 20, 100, 4),
('Томатный', 20, 100, 5),
('барбекю', 20, 100, 5),
('1000 островов', 20, 100, 5),
('Вареные', 20, 100, 6),
('Жареные', 30, 100, 6)
go

select * from [Ingridient]
go

create table [Supply]
(
	[ID_Supply] [int] not null identity(1,1) primary key,
	[Role_ID] [int] not null references [Role] (ID_Role) on delete cascade,
	[Ingridient_ID] [int] not null references [Ingridient] (ID_Ingridient) on delete cascade,
	[Count_Supply] [int] not null,
	[Cost_Supply] [int] not null,
	[Sum_Supply] [int] not null
)
go

insert into [Supply] ([Role_ID], [Ingridient_ID], [Count_Supply], [Cost_Supply], [Sum_Supply]) values
(1, 1, 20, 20, 400)
go

select * from [Supply]
go

create table [dbo].[Dish_Ingridient]
(
  [ID_Dish_Ingridient] [int] not null identity(1,1),
  [Dish_ID] [int] not null,
  [Ingridient_ID] [int] not null,
  constraint [FK_Dish_Dish_Ingridient] foreign key ([Dish_ID])
  references [dbo].[Dish] ([ID_Dish]),
  constraint [FK_Ingridient_Dish_Ingridient] foreign key ([Ingridient_ID])
  references [dbo].[Ingridient] ([ID_Ingridient]),
  constraint [PK_Dish_Ingridient] primary key clustered 
  ([ID_Dish_Ingridient] ASC) on [PRIMARY]
)
insert into [dbo].[Dish_Ingridient]([Dish_ID], [Ingridient_ID])
values (1 , 1),
(1 , 4),
(1 , 7),
(1 , 10),
(1 , 13),
(1 , 16)

create table [Cheque]
(
	[ID_Cheque] [int] not null identity(1,1) primary key,
	[User_ID] [int] not null references [User] (ID_User) on delete cascade,
	[Count_Dish] [int] not null,
	[Cost_Dish] [int] not null,
	[Sum_Order] [int] not null,
	[Time_Order] [datetime] not null,
	[Ear] [bit] not null,
	[Noticed] [bit] not null
)
go

insert into [Cheque] ([User_ID], [Count_Dish], [Cost_Dish], [Sum_Order], [Time_Order], [Ear], [Noticed]) values
(1, 1, 290, 290, SYSDATETIME(), 0, 0)
go

select * from [Cheque]
go

create table [Cheque_Dish]
(
	[ID_Cheque_Dish] [int] not null identity(1,1) primary key,
	[Cheque_ID] [int] not null references [Cheque] (ID_Cheque) on delete cascade,
	[Dish_Cheque_ID] [int] not null references [Dish] (ID_Dish) on delete cascade
)
go

insert into [Cheque_Dish] ([Cheque_ID], [Dish_Cheque_ID]) values
(1,1)
go

select * from [Cheque_Dish]
go