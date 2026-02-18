#!C:/Python310/python.exe
import sys
import cgi
import cgitb
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type:text/html; charset=utf-8\n")

form = cgi.FieldStorage()
FId = form.getvalue("fid")

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="cropshield",
    ssl_disabled=True,
    use_pure=True
)

if FId:
    mycursor = mydb.cursor()
    query = f""" SELECT * FROM farmerlogin WHERE FId = {FId}"""
    # print(query)
    mycursor.execute(query)
    myresult = mycursor.fetchone()
    # print(myresult)

    # Fetch recent history (latest 6 queries) for this farmer (simple query)
    mycursor.execute(f"SELECT FQId, CropName, PartName, SymptomsDetails, SImg, QueryStatus FROM farmerquery WHERE FId = {FId} ORDER BY FQId DESC LIMIT 6")
    history = mycursor.fetchall()

    import header
    print("""
        <style>
        .fa {
            display: inline-block;
            font: normal normal normal 14px / 1 FontAwesome;
            font-size: inherit;
            text-rendering: auto;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
    </style>  
        """)
    print(f"""

        <!-- SECTION: Profile -->
        <form action="profileEdit.py" method="POST" style="margin:50px;">
            <div class="container">
                <div class="row" style="margin-top:30px;">
                    <!-- Profile Card -->
                    <div class="col-md-4 col-xs-12">
                        <div style="border-radius:20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-bottom: 20px; border: 1px solid transparent; padding:30px;">
                            <div class="panel-body text-center">
                                <div style="position:relative;">
                                    <img src="html/ltr/assets/userImg/{myresult[0]}/{myresult[1]}" alt="Profile Picture" class="img-circle" style="width:100px; height:100px; object-fit:cover; border:2px solid #eee; border-radius: 50%;">
                                    <span hidden style="position:absolute; top:10px; right:10px; background:#fff; border-radius:50%; padding:5px;box-shadow:0 1px 4px rgba(0,0,0,0.1);"><i class="fa fa-camera"></i></span>
                                </div>
                                <div>
                                    <h3 style="margin-top:15px; color:#333; font-weight:700;">{myresult[2]}</h3>
                                    <p>Premium Member</p>
                                </div>
                                <div style="margin:15px 0;">
                                    <div style="display:inline-block; background:#2980b9; color:#fff; font-weight:700; font-size:18px; padding:3px 18px; border-radius:5px;">
                                        <i class="fa fa-id-card"></i>
                                        <input type="text" id="Id" name="Id" style="background:transparent; border:none; color:#fff; font-weight:700; width:110px; text-align:center;" value="{myresult[0]}" readonly>
                                    </div>
                                </div>
                                <button type="submit" class="btn btn-primary btn-block" style="font-size:18px;"><i class="fa fa-edit"></i> Edit Profile</button>
                                <a href="SendOTP.py?email={myresult[3]}&fid={FId}" class="btn btn-primary btn-block" style="font-size:18px;"><i class="fa fa-key"></i> Password</a>
                                
                            </div>
                        </div>
                    </div>
                    
                    <!-- Personal Info & Quick Actions -->
                    <div class="col-md-8 col-xs-12">
                        <div style="border-radius:20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); background-color: #fff; border: 1px solid transparent; padding:0px;">
                            <div style="padding: 15px;">
                                <h3><i class="fa fa-user-circle"></i> Personal Information</h3>
                                <hr>
                                <div class="row" style="margin-bottom:20px;">
                                    <div class="col-md-12">
                                        <div class="row" style="margin-bottom:10px;">
                                            <div class="col-sm-1 text-center"><i class="fa fa-envelope fa-2x"></i></div>
                                            <label for="shiping-address">
                                                <small>Email Address</small>
                                            </label><br>
                                            <input style="border:none; padding-left:20px; width:70%;" type="email" id="Email" name="Email" placeholder="Email" value="{myresult[3]}" readonly>
                                        </div>
                                        <div class="row" style="margin-bottom:10px;">
                                            <div class="col-sm-1 text-center"><i class="fa fa-phone fa-2x"></i></div>
                                            <label for="shiping-address">
                                                <small>Phone Number</small>
                                            </label><br>
                                            <input style="border:none; padding-left:20px; width:70%;" type="tel" id="PhoneNo" name="PhoneNo" placeholder="PhoneNo" value="{myresult[4]}" readonly>
                                        </div>
                                        <div class="row" style="margin-bottom:10px;">
                                            <div class="col-sm-1 text-center"><i class="fa fa-phone fa-2x"></i></div>
                                            <label for="shiping-address">
                                                <small>Address</small>
                                            </label><br>
                                            <input style="border:none; padding-left:20px; width:70%;"  type="text" id="Address" name="Address" placeholder="Address" value="{myresult[6]}" readonly>
                                        </div>
                                        <div class="row" style="margin-bottom:10px;">
                                            <div class="col-sm-1 text-center"><i class="fa fa-map-marker fa-2x"></i></div>
                                            <label for="shiping-address">
                                                <small>Distric</small>
                                            </label><br>
                                            <input style="border:none; padding-left:20px; width:70%;" type="text" id="Distric" name="Distric" placeholder="Distric" value="{myresult[7]}" readonly>
                                        </div>
                                        <div class="row" style="margin-bottom:10px;">
                                            <div class="col-sm-1 text-center"><i class="fa fa-map-marker fa-2x"></i></div>
                                            <label for="shiping-address">
                                                <small>State</small>
                                            </label><br>
                                            <input style="border:none; padding-left:20px; width:70%;" type="text" id="State" name="State" placeholder="State" value="{myresult[8]}" readonly>
                                        </div>
                                    </div>
                                </div>
                                <hr>
                                <h4><i class="fa fa-bolt"></i> Quick Actions</h4>
                                <div class="row" style="margin-top:15px;">
                                    <div class="col-sm-6">
                                        <a href="dashboard.py?fid={FId}" class="btn btn-block" style="background:#ff5e3a;color:#fff;font-size:18px;padding:18px 0;border-radius:12px;"><i class="fa fa-tachometer-alt"></i> Dashboard</a>
                                    </div>
                                    <div class="col-sm-6">
                                        <a href="myhistory.py?fid={FId}" class="btn btn-block" style="background:#ff4f8b;color:#fff;font-size:18px;padding:18px 0;border-radius:12px;"><i class="fa-solid fa-file-export"></i> My History</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </form>
        <!-- /SECTION: Profile -->
    """)

    import footer
else:
    print(f'''
        <script>
        alert(" You are not loged In!");
        location.href="login.py?";
        </script>
    ''')
