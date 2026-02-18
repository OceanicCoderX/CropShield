#!C:/Python310/python.exe
import sys
import cgi
import cgitb
import os
import mysql.connector
import smtplib
import random
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type:text/html; charset=utf-8\n")
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
# print(form)
QId = form.getvalue("QId")
Question = form.getvalue("que")
Answer = form.getvalue("ans")
product = form.getvalue("ProName")

query = f"""INSERT INTO replayquery (FQId, Question, Answer, Position, SuggestProduct) VALUES ('{QId}', '{Question}', '{Answer}','public', '{product}')"""
Qstatus = f"UPDATE farmerquery SET QueryStatus = 'Replied' WHERE FQId = {QId};"

mycursor.execute(query)
mycursor.execute(Qstatus)
mydb.commit()

sender_email = "oceanprincess003@gmail.com"
receiver_email = form.getvalue("Email")
password = "sqzb uvyu ihwh smaw"

# Create the email content
subject = "- 🌱 Good News! CropShield Responded to Your Query "
body = f"""
        Hello Farmer🙏,

        We’re happy to inform you that the admin has responded to your query. Please visit the link below to read the full reply:
        
        🔗 **Website link:** https://cropshield.com

        Thank you for reaching out! If you need further assistance, feel free to contact us anytime.

        Best wishes 🌱,
        Team CropShield
"""

# Build the message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Send the email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        print(f'''
            <script>
                alert("Replay Query Successfully! Query is now in Public");
                location.href="QueryList.py";
            </script>
        ''')
except Exception as e:
    print("Error:", e) 
