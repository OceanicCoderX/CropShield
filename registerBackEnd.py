#!C:/Python310/python.exe
import sys
import cgi
import cgitb
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type:text/html; charset=utf-8\n")

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="cropshield",
    ssl_disabled=True,
    use_pure=True
)
mycursor = mydb.cursor()

form = cgi.FieldStorage()
# print(form)
Name = form.getvalue("name")
Email = form.getvalue("email")
PhoneNo = form.getvalue("phone")
Password = form.getvalue("password")
Address = form.getvalue("address")
Distric = form.getvalue("district")
State = form.getvalue("state")

query = f"""INSERT INTO farmerlogin (Name, Email, PhoneNo, Password, Address, Distric, State) VALUES ('{Name}','{Email}', '{PhoneNo}', '{Password}','{Address}', '{Distric}', '{State}')"""
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
   <script>
   alert(" Ragister Successfully!");
   location.href="login.py";
   </script>''')