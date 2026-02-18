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
notp = form.getvalue("otp")
Email = form.getvalue("email")
FId = form.getvalue("fid")
otp = form.getvalue("otp")

if notp == otp:
    print(f'''
        <script>
            alert(" OTP verified successfully!");
            location.href="changepassword.py?&fid={FId}";
        </script>
    ''')
else:
    print(f'''
        <script>
            alert(" Invalid OTP! Please try again.");
            location.href="EnterOTP.py?email={Email}&fid={FId}";
        </script>
    ''')