#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import sys
import cgi
import cgitb
import os
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
FId = form.getvalue("fid")
Email = form.getvalue("Email")
NewPassword = form.getvalue("NewPassword")

query = f"UPDATE farmerlogin SET Password = '{NewPassword}' WHERE Email = '{Email}'"
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Passwrd Change Successfully!");
    location.href="myaccount.py?fid={FId}";
    </script>''')
