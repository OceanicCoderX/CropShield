#!C:/Python310/python.exe
import sys
import cgi
import cgitb
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
# print("Content-Type:text/html; charset=utf-8\n")

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

query = f""" SELECT * FROM company"""
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchone()
# print(myresult)
import header
print(f"""
        <div class="page-wrapper">
            <div class="container-fluid">
                <!-- row -->
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">Company Form</h4>
                                <form class="m-t-30" action="CompanyUpdate.py" method="POST" enctype="multipart/form-data">
                                    <input class="form-control" id="Id" name="Id" value="{myresult[0]}" hidden>
                                    <div class="form-group">
                                        <label for="Image">Company Logo</label><br>
                                        <img src="assets/Logo/{myresult[0]}/{myresult[2]}" style="width: 100px; height: 100px;"> &nbsp;&nbsp;&nbsp;
                                        <input type="file" id="Image" name="Image">
                                        <input type="hidden" id="OldImage" name="OldImage" value="{myresult[2]}">
                                    </div>
                                    <div class="form-group">
                                        <label for="Name">Company Name</label>
                                        <input type="text" class="form-control" id="Name" name="Name" aria-describedby="emailHelp" value="{myresult[1]}">
                                    </div>    
                                    <div class="form-group">
                                        <label for="Email">Email</label>
                                        <input type="Email" class="form-control" id="Email" name="Email" aria-describedby="emailHelp" value="{myresult[3]}">
                                    </div>    
                                    <div class="form-group">
                                        <label for="PhoneNo">Phone Number</label>
                                        <input type="tel" class="form-control" id="PhoneNo" name="PhoneNo" aria-describedby="emailHelp" value="{myresult[4]}">
                                    </div>   
                                    <div class="form-group">
                                        <label for="Address">Address</label>
                                        <input type="text" class="form-control" id="Address" name="Address" aria-describedby="emailHelp" value="{myresult[5]}">
                                    </div>  
                                    <div class="form-group">
                                        <label for="GSTno">GST number</label>
                                        <input type="text" class="form-control" id="GSTno" name="GSTno" aria-describedby="emailHelp" value="{myresult[6]}">
                                    </div>                                                   
                                    <button type="submit" class="btn btn-primary">Edit Details</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>                
            </div>
        </div>
""")
import footer