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
Email = form.getvalue('Email')
Password = form.getvalue('Password')

try:
    query =f"""SELECT * FROM adminlogin WHERE Email = '{Email}' AND Password = '{Password}'"""
    mycursor.execute(query)
    myresult = mycursor.fetchone()
    # print(mycursor.rowcount)
    
    if mycursor.rowcount == 1:
        AId = myresult[0]
        AdminName = myresult[1]
        PhoneNo = myresult[4]
        print(f'''
        <script>
        localStorage.clear();
        localStorage.setItem("AId", "{AId}");
        localStorage.setItem("AdminName", "{AdminName}");
        localStorage.setItem("PhoneNo", "{PhoneNo}");
        localStorage.setItem("Email", "{Email}");
        alert("Login Successfully!");
        location.href="Dashboard.py";
        </script>''')
    else:
        print(f'''
        <script>alert("Invalid Email or Password!");
        location.href="AdminLogin.py";
        </script>''')
        
except mysql.connector.Error as err:
    print(f"""
    <script>
        alert(" Database Error: {str(err)}");
        window.location.href = "AdminLogin.py";
    </script>
    """)