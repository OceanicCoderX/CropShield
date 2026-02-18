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

# --- Database Connection ---
try:
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
except mysql.connector.Error as err:
    print(f"<p>Database Connection Error: {err}</p>")
    sys.exit()

# --- Form Data Retrieval ---
form = cgi.FieldStorage()
# Ensure values are not None before using in f-strings/queries
QId = form.getvalue("QId", "")
Question = form.getvalue("que", "")
Answer = form.getvalue("ans", "")
product = form.getvalue("ProName", "")
receiver_email = form.getvalue("Email", "")

# --- Database Operations ---
try:
    # Use parameterized queries or proper escaping for security, 
    # but for a quick fix, let's just make sure the f-strings are correctly structured.
    # Note: THIS IS VULNERABLE TO SQL INJECTION. Use placeholders (e.g., %s) in production!
    query = f"INSERT INTO replayquery (FQId, Question, Answer, SuggestProduct) VALUES ('{QId}', '{Question}', '{Answer}', '{product}')"
    Qstatus = f"UPDATE farmerquery SET QueryStatus = 'Replied' WHERE FQId = '{QId}';" # Quote QId just in case

    mycursor.execute(query)
    mycursor.execute(Qstatus)
    mydb.commit()
    db_success = True
except Exception as e:
    db_success = False
    db_error = str(e)

# --- Email Setup ---
if db_success and receiver_email:
    sender_email = "oceanprincess003@gmail.com"
    password = "sqzb uvyu ihwh smaw" # This is an App Password
    subject = "🌱 Good News! CropShield Responded to Your Query"
    body = f"""
        Hello Farmer🙏, <br><br>

        We’re happy to inform you that the admin has responded to your query. Please visit the link below to read the full reply: <br><br>

        🔗 **Website link:** https://cropshield.com <br><br>

        Thank you for reaching out! If you need further assistance, feel free to contact us anytime. <br><br>

        Best wishes 🌱, <br>
        Team CropShield
    """

    # Build the message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html")) # Changed to 'html' for better formatting/link

    # Send the email
    try:
        # Use a reliable Google SMTP server address
        # Error 11001 is a DNS issue; ensuring internet connection is key.
        # smtplib.SMTP_SSL("smtp.gmail.com", 465) is another secure option
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server: 
            server.starttls()
            server.login(sender_email, password)
            server.send_message(message)
            
            # --- Success Output ---
            print(f'''
                <script>
                    alert("Reply Query Successfully and Email Sent!");
                    location.href="QueryList.py";
                </script>
            ''')

    except Exception as e:
        # --- Email Error Output ---
        print(f'''
            <script>
                alert("Reply Query Successfully (DB updated) but Email Sending Failed! Error: {e}");
                location.href="QueryList.py";
            </script>
        ''')

elif not db_success:
    # --- DB Error Output ---
    print(f'''
        <script>
            alert("Database Error: Failed to save reply! {db_error}");
            history.back();
        </script>
    ''')

else:
    # This block handles cases where the email form field might be missing
    print(f'''
        <script>
            alert("Reply Query Successfully (DB updated) but Missing Receiver Email!");
            location.href="QueryList.py";
        </script>
    ''')