import mysql.connector as mysql
from tabulate import tabulate
import datetime

def show():
    conn = mysql.connect(host="localhost",user="root",password="",database="mulesoft")
    cur = conn.cursor()
    cur.execute("SELECT name, release_date, director, lead_actor, lead_actress FROM movies ORDER BY release_date ASC")
    records = cur.fetchall()
    head = ["Name", "Release Date","Director","Actors","Actress"]
    print("All Movies: ")
    print(tabulate(records, headers=head, tablefmt="grid"))
    cur.execute("commit")
    conn.close()

def find(query):
    conn = mysql.connect(host="localhost",user="root",password="",database="mulesoft")
    cur = conn.cursor()
    cur.execute("SELECT name, release_date, director, lead_actor, lead_actress FROM movies where lead_actor LIKE '%" + query +"%' or lead_actress LIKE '%" + query +"%' ORDER BY release_date ASC")
    records = cur.fetchall()
    head = ["Name", "Release Date","Director","Actors","Actress"]
    print("Search Results: ")
    print(tabulate(records, headers=head, tablefmt="grid"))
    cur.execute("commit")
    conn.close()

def insert(name,release_date,director,actor,actress):
    conn = mysql.connect(host="localhost", user="root", password="", database="mulesoft")
    cur = conn.cursor()
    cur.execute("INSERT INTO movies (name,release_date,director,lead_actor,lead_actress) VALUES (%s,%s,%s,%s,%s)", (name, release_date, director, actor,actress))
    print("Data Inserted!!!")
    cur.execute("commit")
    conn.close()

print('Welcome...')
repeat = 1
while(repeat):
    print("\n")
    print("*****MENU******")
    print("1. Show all Movies")
    print("2. Search by name")
    print("3. Insert a movie")
    print("4. Enter '-1' to exit")
    choice = int(input("Enter Your Choice: "))
    print("\n")
    if choice==1:
        show()
    elif choice==2:
        query = input("Enter your query: ")
        find(query)
    elif choice==3:
        name = input("Enter Movie Name: ")
        release_date = input("Release date in YYYY-MM-DD format: ")
        director = input("Director Name: ")
        actor = input("Lead Actor Name: ")
        actress = input("Actress Name: ")
        insert(name,release_date,director,actor,actress)
    elif choice==-1:
        repeat=0
    else:
        print("Invalid Choice")
