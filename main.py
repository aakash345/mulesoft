from logging import exception
import mysql.connector as mysql
from tabulate import tabulate
import datetime

def createdb():
    conn = mysql.connect(host="localhost", user="root", password="")
    cur = conn.cursor()
    try:
        cur.execute("CREATE DATABASE mulesoft")
        print("Database Created!")
    except Exception as e:
        conn.rollback()
        # print(e)
        print("Database already exist")
    finally:
        cur.execute("commit")
        conn.close()
def createtable():
    conn = mysql.connect(host="localhost", user="root", password="",database="mulesoft")
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE movies ( id int(50) NOT NULL auto_increment, name varchar(50), release_date date, director varchar(100), lead_actor varchar(50), lead_actress varchar(50), PRIMARY KEY(id) );")
    except Exception as e:
        conn.rollback()
        # print(e)
        print("Table already exist")
    finally:
        cur.execute("commit")
        conn.close()

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
    try:
        cur.execute("SELECT name, release_date, director, lead_actor, lead_actress FROM movies where lead_actor LIKE '%" + query +"%' or lead_actress LIKE '%" + query +"%' ORDER BY release_date ASC")
        records = cur.fetchall()
        if records:
            head = ["Name", "Release Date","Director","Actors","Actress"]
            print("Search Results: ")
            print(tabulate(records, headers=head, tablefmt="grid"))
        else:
            print("No results found..")
    except Exception as e:
        print(e)
    finally:
        cur.execute("commit")
        conn.close()

def insert(name,release_date,director,actor,actress):
    conn = mysql.connect(host="localhost", user="root", password="", database="mulesoft")
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO movies (name,release_date,director,lead_actor,lead_actress) VALUES (%s,%s,%s,%s,%s)", (name, release_date, director, actor,actress))
        print("Data Inserted!!!")
    except Exception as e:
        print(e)
    finally:
        cur.execute("commit")
        conn.close()

print('Welcome...')
repeat = 1
while(repeat):
    print("\n")
    print("*****MENU******")
    print("1. Create Database")
    print("2. Create Table")
    print("3. Insert a Movie")
    print("4. Show all Movies")
    print("5. Search by Actors name")
    print("6. Enter '-1' to exit")
    choice = int(input("Enter Your Choice: "))
    print("\n")
    if choice==1:
        createdb()
    elif choice==2:
        createtable()
    elif choice==3:
        name = input("Enter Movie Name: ")
        release_date = input("Release date in YYYY-MM-DD format: ")
        director = input("Director Name: ")
        actor = input("Lead Actor Name: ")
        actress = input("Actress Name: ")
        insert(name,release_date,director,actor,actress)
    elif choice==4:
        show()
    elif choice==5:
        query = input("Enter your query: ")
        find(query)
    elif choice==-1:
        repeat=0
    else:
        print("Invalid Choice")
