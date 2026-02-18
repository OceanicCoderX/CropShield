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
Id = form.getvalue("fid")
Status = form.getvalue("status")

if Status == "Active":
    new_status = "Blocked"
else:
    new_status = "Active"

query = f"UPDATE farmerlogin SET Status = '{new_status}' WHERE FId = {Id}"
# print(query)
mycursor.execute(query)
mydb.commit()

if new_status == "Blocked":
    print("""
    <script>
        alert('Farmer Blocked!');
        location.href="FarmerList.py";
    </script>""")
else:
    print("""
    <script>
        alert('Farmer Unblocked!');
        location.href="FarmerList.py";
    </script>""")
