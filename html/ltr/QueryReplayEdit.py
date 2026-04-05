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
FQId = form.getvalue("qid")

query = f"""SELECT fq.FQId, fq.FId, fl.Image AS FarmerImage, fl.Name AS FarmerName, fl.Email AS FarmerEmail, fq.FarmerName, c.CropName , p.Name , fq.SymptomsDetails, fq.SImg, fq.QueryStatus
            FROM farmerlogin fl JOIN farmerquery fq ON fl.FId = fq.FId JOIN crops c ON fq.CropName = c.CropId JOIN parts p ON fq.PartName = p.PartId 
            WHERE fq.FQId = {FQId};"""
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchone()

replayquery = f"SELECT * FROM replayquery WHERE FQId = {FQId};"
mycursor.execute(replayquery)
replay = mycursor.fetchone()

pro_query = "SELECT * FROM product"
mycursor.execute(pro_query)
product = mycursor.fetchall()
pro_op= ""
for pro in product:
    selected = "selected" if str(pro[0]) == str(replay[5]) else ""
    pro_op += f'''
        <option value="{pro[0]}" {selected}>{pro[3]}</option>
    '''
    
import header
print(f"""
      
        <div class="page-wrapper">
            <div class="email-app">
                
                <div class="mail-details bg-white">
                    <div class="card-body border-bottom">
                        <h4 class="m-b-0">Farmer Query</h4>
                    </div>
                    <div class="card-body border-bottom">
                        <div class="d-flex no-block align-items-center m-b-40">
                            <div class="m-r-10"><img src="assets/userImg/{myresult[1]}/{myresult[2]}" alt="user" class="rounded-circle" width="45"></div>
                            <div class="">
                                <h5 class="m-b-0 font-16 font-medium">{myresult[3]} <small> ( {myresult[4]} )</small></h5>
                            </div>
                        </div>
                        <h4 class="m-b-15">Crop Name: {myresult[6]}</h4>
                        <h4 class="m-b-15">Crop Name: {myresult[7]}</h4>
                        <p>{myresult[8]}</p>
                    </div>
                    <div class="card-body">
                        <h4><i class="fa fa-paperclip m-r-10 m-b-10"></i> Attachments</h4>
                        <div class="row">
                            <div class="col-md-2">
                                <a href="javascript:void(0)"> <img class="img-thumbnail img-responsive" alt="attachment" src="assets/FqueryImg/{myresult[0]}/{myresult[9]}"> </a>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Replay part -->
                
                <div class="mail-compose bg-white">
                    <div class="p-20 border-bottom">
                        <div class="d-flex align-items-center">
                            <div>
                                <h4>Replay Message</h4>
                                <span>create new message</span>
                            </div>
                            <div class="ml-auto">
                                <a id="cancel_compose" class="btn btn-dark" href="FarmerQuery.py" style="color:White">Back</a>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Action part -->
                    <!-- Button group part -->
                    <div class="card-body">
                        <form action="queryUpdate.py" method="POST" enctype="multipart/form-data">
                            <div class="form-group">
                                <input type="text" id="QId" name="QId" hidden value="{FQId}">
                                <input type="text" id="que" name="que" class="form-control" value="{replay[2]}">
                            </div>
                            <div class="form-group">
                                <textarea name="ans" id="ans" style="border: 2px solid #e1e1e1; color: #555555; padding: 20px; width: 100%; height: 165px; border-radius: 5px;">{replay[3]}</textarea>
                            </div>
                            <div class="form-group mb-3">
                                <label for="DseName">Product Name</label>
                                <select class="form-control" id="ProName" name="ProName" required>
                                    <option value="">- Select Product -</option>
                                    {pro_op}
                                </select>
                            </div> 
                            <button type="submit" class="btn btn-success m-t-20"><i class="far fa-envelope"></i> Send Privatly</button>
""")
btn_class = 'btn-success' if {myresult[9]} == 'public' else 'btn-secondary'
btn_label = 'Public' if {myresult[9]} == 'public' else 'Send Publicly'
    
print(f"""
                            
                            
                            <form action="queryposition.py" method="POST" style="display:inline-block;">
                                <input type="hidden" name="fqid" id="fqid" value="{FQId}">
                                <input type="hidden" name="pos" id="pos" value="{myresult[9]}">
                                <button type="submit" class="btn btn-dark m-t-20 {btn_class}">{btn_label}</button>
                            </form>
                        </form>
                        <!-- Action part -->
                    </div>
                </div>
            </div>
        </div>
        
""")
import footer
