#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
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
FId = form.getvalue("fid")

query = f""" SELECT Email, Password FROM farmerlogin WHERE FId = {FId}"""
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchone()
# print(myresult)

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
                            <form id="changePwdForm" action="passwordBackEnd.py" method="POST">
                                <input type="fid" class="form-control" id="fid" name="fid" value="{FId}" hidden>
                                <div class="form-group">
                                    <label for="Email">Email or Username</label>
                                    <input type="email" class="form-control" id="Email" name="Email" value="{myresult[0]}" readonly>
                                </div>
                                <div class="form-group mb-3">
                                    <label for="NewPassword">New Password</label>
                                    <input type="password" class="form-control" id="NewPassword" name="NewPassword" placeholder="Enter New password" required>
                                </div>
                                <div class="form-group mb-3">
                                    <label for="ConfirmPassword">Confirm Password</label>
                                    <input type="password" class="form-control" id="ConfirmPassword" name="ConfirmPassword" placeholder="Confirm password" required>
                                </div>
                                <button type="submit" id="changePwdBtn" class="btn btn-block" style="background:#e53935;color:#fff;font-weight:600;border-radius:6px;" disabled>Set Password</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
""")
print("""
      <script>
            var newPwd = document.getElementById('NewPassword');
            var confirmPwd = document.getElementById('ConfirmPassword');
            var btn = document.getElementById('changePwdBtn');
            var form = document.getElementById('changePwdForm');
            function checkPasswords() {
                if (newPwd.value && confirmPwd.value && newPwd.value === confirmPwd.value) {
                    btn.disabled = false;
                } else {
                    btn.disabled = true;
                }
            }
            newPwd.addEventListener('input', checkPasswords);
            confirmPwd.addEventListener('input', checkPasswords);
            confirmPwd.addEventListener('input', function() {
                if (newPwd.value && confirmPwd.value && newPwd.value === confirmPwd.value) {
                    btn.disabled = false;
                    // Auto-submit when both match
                    // form.submit();
                }
            });
        </script>
    """)
