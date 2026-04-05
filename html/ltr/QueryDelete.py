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
    host="localhost",  # IMPORTANT: use IP, not 'localhost'
    port="3306",
    user="root",
    password="",
    database="cropshield",
    ssl_disabled=True,  # disables SSL completely (recommended for local dev)
    use_pure=True
)
mycursor = mydb.cursor()

form = cgi.FieldStorage()
QId = form.getvalue("qid")

query1 = f"DELETE FROM replayquery WHERE RQId = {QId}"
query2 = f"UPDATE farmerquery SET QueryStatus = 'Panding' WHERE FQId = {QId}"
mycursor.execute(query1)
mycursor.execute(query2)
mydb.commit()
print(f'''
    <script>alert(" Query Delete Successfully!");
    location.href="QueryList.py";
    </script>''')
