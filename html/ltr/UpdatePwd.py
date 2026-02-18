#!C:/Python310/python.exe
import sys
import cgi
import cgitb
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
Email = form.getvalue("Email")
Password = form.getvalue("Password")
# print(Password)

query = f"UPDATE adminlogin SET Password={Password} WHERE Email='{Email}'"
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>
    alert("Reset Password Successfully!");
    location.href="AdminLogin.py";
    </script>''')