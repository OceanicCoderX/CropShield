#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import cgi
import cgitb
import os
import mysql.connector
import smtplib
import random
cgitb.enable()
print("Content-Type:text/html\n")
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
Email = form.getvalue("email")

query = f""" SELECT * FROM adminlogin WHERE Email = '{Email}'"""
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchone()
# print(myresult)

if(myresult):

    # Step 1: Generate a random 6-digit OTP
    otp = str(random.randint(100000, 999999))
    # print(otp)

    # Step 2: Email configuration
    sender_email = "oceanprincess003@gmail.com"
    receiver_email = Email
    password = "sqzb uvyu ihwh smaw"  # Use App Password, not your Gmail password!

    # Step 3: Create the email content
    subject = "Your OTP Verification Code"
    body = f"Your One-Time Password (OTP) is: {otp}\n\n Please do not share this with anyone."

    # Step 4: Build the message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Step 5: Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(message)
            print(f'''
                <script>
                    alert(" OTP sent successfully! Check your email.");
                    location.href="CheckOTP.py?otp={otp}&email={receiver_email}";
                </script>
            ''')
    except Exception as e:
        print("Error:", e) 

else:
    print(f'''
    <script>alert("Invalid Email!");
    location.href="AdminLogin.py";
    </script>''')
