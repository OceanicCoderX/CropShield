#!C:/Python310/python.exe
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


query = f"SELECT QueryStatus FROM farmerquery WHERE FQId = {QId}"
mycursor.execute(query)
myresult = mycursor.fetchone()

Status = ''
if myresult and myresult[0] is not None:
    Status = str(myresult[0])

# normalize status (strip spaces, case-insensitive)
status_clean = Status.strip()
# print(status_clean)

if status_clean in ('Panding'):
    print(f'<script> location.href="QueryDetail.py?qid={QId}"; </script>')
else:
    print(f'<script> location.href="QueryReplayEdit.py?qid={QId}"; </script>')
