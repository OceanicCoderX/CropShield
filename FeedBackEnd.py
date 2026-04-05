#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
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
email = form.getvalue('email')
star = form.getvalue('rating')
message = form.getvalue('message')

query = f"""SELECT FId FROM farmerlogin WHERE Email= '{email}'"""
mycursor.execute(query)
myresult = mycursor.fetchone()
# print(myresult)

if myresult:
    insert_query = f"""INSERT INTO feedback (FId, FeedBack, Star) VALUES ('{myresult[0]}', '{message}', '{star}')"""
    mycursor.execute(insert_query)
    mydb.commit()
    print(f'''
        <script>
        alert(" Feedback Submit Successfully!");
        location.href="testimonials.py";
        </script>''')
else:
    print(f'''
        <script>
        alert(" You are Not Register! Register first");
        location.href="testimonials.py";
        </script>''')
