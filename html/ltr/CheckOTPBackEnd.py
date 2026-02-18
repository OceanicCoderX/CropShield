#!C:/Python310/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-Type:text/html\n")

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

form = cgi.FieldStorage() # value pass from CheckOTP.py
Email = form.getvalue("Email")
notp = form.getvalue("notp")
otp = form.getvalue("otp")
# print(form)

if notp == otp:
    print(f'''
        <script>
            alert(" OTP verified successfully!");
            location.href="ResetPassword.py?email={Email}";
        </script>
    ''')
else:
    print(f'''
        <script>
            alert(" Invalid OTP! Please try again.");
            location.href="CheckOTP.py?email={Email}";
        </script>
    ''')