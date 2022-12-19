import mysql.connector
con = mysql.connector.connect(
    host="localhost", user="root", passwd="Yash@12345")
c = con.cursor()


sql1 = "create database cadatabase"
c.execute(sql1)
sql2 = "use cadatabase"
c.execute(sql2)
sql3 = "create table checkin(days varchar(50),names varchar(20),age varchar(20),date varchar(20),typenumber varchar(20))"
c.execute(sql3)
sql4 = "create table checkout(typenumber varchar(20),guests integer, fare integer,tbill integer,date varchar(20))"
c.execute(sql4)
con.commit()
