#!C:/Python310/python.exe
import sys
import cgi
import cgitb
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type:text/html; charset=utf-8\n")

form = cgi.FieldStorage()
FId = form.getvalue("Id")

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

query = f""" SELECT * FROM farmerlogin WHERE FId = {FId}"""
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchone()
# print(myresult)

import header

print(f"""

    <!-- SECTION: Profile -->
    <form action="profileUpdate.py" method="POST" enctype="multipart/form-data">
        <div class="container " style="margin-top:30px;">
            
            <div class="panel panel-default" style="border-radius:20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
                <div class="panel-body text-center" style="margin:30px;">
                    <h3 style="padding:15px;"><i class="fa fa-user-circle"></i> Personal Information</h3>
                    <hr>
                    <div class="row" style="margin-bottom:20px;">
                        <div class="col-md-12">    
                                                
                            <div style="position:relative;">
                                <img src="html/ltr/assets/userImg/{myresult[0]}/{myresult[1]}" alt="Profile Picture" class="img-circle" style="width:100px; height:100px; border-radius:50px; object-fit:cover; border:2px solid #eee;">
                                <input type="hidden" id="OldImg" name="OldImg" style="display:none;" value="{myresult[1]}">
                                <label for="UserImg" style="position:absolute; top:10px; right:10px; background:#fff; border-radius:50%; padding:5px; box-shadow:0 1px 4px rgba(0,0,0,0.1); cursor:pointer;">
                                    <i class="fa fa-camera"></i>
                                </label>
                                <input type="file" id="UserImg" name="UserImg" style="display:none;">
                            </div>
                            
                            <div style="margin:15px 0;">
                                <div style="display:inline-block; background:#2980b9; color:#fff; font-weight:700; font-size:18px; padding:3px 18px; border-radius:5px;">
                                    <i class="fa fa-id-card"></i>
                                    <input type="text" id="Id" name="Id" style="background:transparent; border:none; color:#fff; font-weight:700; width:110px; text-align:center;" value="{myresult[0]}" readonly>
                                </div>
                            </div>
                        
                            <div class="row" style="margin-bottom:10px;">
                                <div class="col-sm-1 text-center"><i class="fa fa-user fa-2x"></i></div>
                                <label for="shiping-address">
                                    <small>Name :</small>
                                </label><br>
                                <input style="border:none; margin-left:20px; width:70%;" type="text" id="Name" name="Name" placeholder="Name" value="{myresult[2]}">
                            </div>
                            <div class="row" style="margin-bottom:10px;">
                                <div class="col-sm-1 text-center"><i class="fa fa-envelope fa-2x"></i></div>
                                <label for="shiping-address">
                                    <small>Email Address</small>
                                </label><br>
                                <input style="border:none; margin-left:20px; width:70%;" type="email" id="Email" name="Email" placeholder="Email" value="{myresult[3]}">
                            </div>
                            <div class="row" style="margin-bottom:10px;">
                                <div class="col-sm-1 text-center"><i class="fa fa-mobile fa-2x"></i></div>
                                <label for="shiping-address">
                                    <small>Phone Number</small>
                                </label><br>
                                <input style="border:none; margin-left:20px; width:70%;" type="tel" id="PhoneNo" name="PhoneNo" placeholder="PhoneNo" value="{myresult[4]}">
                            </div>
                            <div class="row" style="margin-bottom:10px;">
                                <div class="col-sm-1 text-center"><i class="fa fa-phone fa-2x"></i></div>
                                <label for="shiping-address">
                                    <small>Address</small>
                                </label><br>
                                <input style="border:none; margin-left:20px; width:70%;"  type="text" id="Address" name="Address" placeholder="Address" value="{myresult[6]}">
                            </div>
                            <div class="row" style="margin-bottom:10px;">
                                <div class="col-sm-1 text-center"><i class="fa fa-map-marker fa-2x"></i></div>
                                <label for="shiping-address">
                                    <small>Distric</small>
                                </label><br>
                                <input style="border:none; margin-left:20px; width:70%;" type="text" id="Distric" name="Distric" placeholder="Distric" value="{myresult[7]}">
                            </div>
                            <div class="row" style="margin-bottom:10px;">
                                <div class="col-sm-1 text-center"><i class="fa fa-map-marker fa-2x"></i></div>
                                <label for="shiping-address">
                                    <small>State</small>
                                </label><br>
                                <input style="border:none; margin-left:20px; width:70%;" type="text" id="State" name="State" placeholder="State" value="{myresult[8]}">
                            </div>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary btn-block" style="font-size:18px;"><i class="fa fa-edit"></i> Update Profile</button>  
                    <br>
                </div>
            </div>
        </div>
    </form>
    <!-- /SECTION: Profile -->
""")
import footer