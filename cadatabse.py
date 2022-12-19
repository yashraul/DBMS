import mysql.connector
con = mysql.connector.connect(
    host="localhost", user="root", passwd="Yash@12345", database="cadatabase")


def checkin():
    d = input("Days:")
    g = input("Names:")
    a = input("Age:")
    dt = input("Date:")
    b = input("Type and number:")
    data = (d, g, a, dt, b)
    sql = 'insert into checkin values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data entered sucessfully")
    main()


def checkout():
    b = input("type and number:")
    tg = int(input("Guests:"))
    f = int(input("fare:"))
    d = int(input("days:"))
    bl = f*d*tg
    cod = input("date:")
    data = (b, tg, f, d, bl, cod)
    sql = 'insert into checkout values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data entered successfully")
    main()


def playground():
    print("volleyball court-100$ ph")
    print("")
    print("""fivb standarad court, gym, ac""")
    print("")
    print("indoor cricket-150# ph")
    print("")
    print("""bat,ball,indoor space""")
    print("")
    print("football-200$ ph")
    print("")
    print("""futsal,changing room, tv""")
    main()


def main():
    print("1. check In")
    print("2.checkout")
    print("3. fare and amenities")
    c = int(input("choice:"))
    if c == 1:
        checkin()
    elif c == 2:
        checkout()
    elif c == 3:
        playground()
    else:
        print("enter correct choice")
    main()


main()
