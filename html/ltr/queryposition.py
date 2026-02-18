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
fqid = form.getvalue('fqid')
Status = form.getvalue('status')
Position = form.getvalue('pos')
# print(Status)

if Status.strip() == 'Panding':
    print(f'''
        <script>
            alert(" Query is Panding! Replay the query first");
            location.href="FarmerQuery.py";
        </script>
    ''')    
else:
    newpos = 'public' if Position != 'public' else 'private'
    query = f"UPDATE replayquery SET position = '{newpos}' WHERE FQId = {fqid}"
    mycursor.execute(query)
    mydb.commit()

    print('<html><head>')
    print('<meta http-equiv="refresh" content="0; URL=QueryList.py" />')
    print('</head><body>')
    print('Updating position...')
    print('</body></html>')
