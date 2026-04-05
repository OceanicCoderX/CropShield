#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
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
PhoneNo = form.getvalue("phone")
Password = form.getvalue("password")

query = f"""SELECT * FROM farmerlogin WHERE PhoneNo = '{PhoneNo}' AND Password = '{Password}'"""
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchone()
# print(myresult)

if myresult:

    FId = myresult[0]
    Name = myresult[2]
    Email = myresult[3]

    if mycursor.rowcount == 1:
        
        
        print(f"""
        <script>
            localStorage.clear();
            localStorage.setItem("FId", '{FId}');
            localStorage.setItem("FName", "{Name}");
            localStorage.setItem("PhoneNo", "{PhoneNo}");
            localStorage.setItem("Email", "{Email}");
            
            alert("LogIn Successfully!");
            location.href="index.py?fid={FId}";
        </script>""")
        
    else:
        print(f'''
        <script>
            alert("Login Unsuccessful! Invalid Email or Password!");
            location.href="login.py";
        </script>''')

else:
    print(f'''
        <script>
            alert("Login Unsuccessful! Invalid Email or Password!");
            location.href="login.py";
        </script>''')
