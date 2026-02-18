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


print("""
<head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel='stylesheet' href='css/bootstrap.min.css'>
    <link rel='stylesheet' href='css/style.css'>
    <style>
        body, html {
            height: 100%;
        }
        .centered-container {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background: #f8f9fa;
        }
        .back-btn {
            display: inline-block;
            margin-bottom: 30px;
            padding: 8px 22px;
            background: #e53935;
            color: #fff;
            border: none;
            border-radius: 6px;
            font-weight: 600;
            font-size: 16px;
            text-decoration: none;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            transition: background 0.2s;
        }
        .back-btn:hover {
            background: #b71c1c;
            color: #fff;
        }
    </style>
</head>
""")
print(f"""
    <div class="centered-container">
        <a href="myaccount.py?fid={FId}" class="back-btn"><i class="fa fa-arrow-left"></i> Back</a>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8 col-lg-6">
                    <div class="card shadow-lg border-0 rounded-lg p-4 mb-4">
                        <div class="card-body">
                            <h3 class="mb-4 text-center" style="color:#e53935;font-weight:700;">Change Password</h3>
                            <form id="changePwdForm" action="CheckOTP.py" method="POST">
                                <input type="fid" class="form-control" id="fid" name="fid" value="{FId}" hidden>
                                <div class="form-group">
                                    <label for="Email">Email or Username</label>
                                    <input type="email" class="form-control" id="Email" name="Email" value="{Email}" readonly>
                                </div>
                                <div class="form-group mb-3">
                                    <label>Enter OTP</label>
                                    <input type="text" value="{notp}" id="notp" name="notp" hidden>
                                    <input type="text" class="form-control" id="otp" name="otp" placeholder="Enter OTP" required>
                                </div>
                                <button type="submit" id="changePwdBtn" class="btn btn-block" style="background:#e53935;color:#fff;font-weight:600;border-radius:6px;">Varify OTP</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
""")
