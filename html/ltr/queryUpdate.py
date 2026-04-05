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
# print(form)
QId = form.getvalue("QId")
Question = form.getvalue("que")
Answer = form.getvalue("ans")
product = form.getvalue("ProName")

query = f"""UPDATE replayquery SET Question='{Question}', Answer='{Answer}', SuggestProduct='{product}' WHERE FQId={QId}"""
Qstatus = f"UPDATE farmerquery SET QueryStatus = 'Replied' WHERE FQId = {QId};"
mycursor.execute(query)
mydb.commit()
print(f'''
        <script>
            alert(" Query Update Successfully!");
            location.href="QueryList.py";
        </script>
    ''')
