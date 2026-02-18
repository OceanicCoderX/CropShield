#!C:/Python310/python.exe
import sys
import cgi
import cgitb
import os
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

mycursor.execute("SELECT f.FQId, f.FId, f.FarmerName, f.SymptomsDetails, f.QueryStatus FROM farmerquery f JOIN replayquery rq ON f.FQId = rq.FQId WHERE rq.Position = 'public' ORDER BY FQId DESC")
myresult = mycursor.fetchall()

tr_html = ''
for x in myresult:
    fqid, fid, fname, sdetails, qstatus = x
    tr_html += f'''
    <tr class="unread">
        <td>{fqid}</td>
        <td class="user-image"><img src="assets/userImg/{fid}/user.jpg" alt="user" class="rounded-circle" width="50"></td>
        <td class="user-name"><h6 class="m-b-0">{fname}</h6></td>
        <td class="max-texts"><a class="link" href="QueryReplayEdit.py?qid={fqid}">
            <span class="blue-grey-text text-darken-4">{(sdetails[:100] + '...') if sdetails and len(sdetails)>100 else (sdetails or '')}</a>
        </td>
        <td class="clip"><b>{qstatus}</b></td>
        <td class="time"><a href="QueryReplayEdit.py?qid={fqid}"><i class="fa-solid fa-reply"></i></a></td>
    </tr>
'''

import header
print(f"""
      
        <div class="page-wrapper">
            <div>
                <div class="mail-list bg-white">
                    <div class="p-15 b-b">
                        <div class="d-flex align-items-center">
                            <div>
                                <h4>Farmers Query </h4>
                                <span>Here is the list of farmer queries</span>
                            </div>
                            <div class="ml-auto">
                                <input placeholder="Search Mail" id="" type="text" class="form-control">
                            </div>
                        </div>
                    </div>
                    <!-- Action part -->
                    
                    <!-- Button group part -->
                    <div class="bg-light p-15 d-flex align-items-center do-block">
                        <div class="btn-group m-t-5 m-b-5">
                            <div class="custom-control custom-checkbox">
                                <input type="checkbox" class="custom-control-input sl-all" id="cstall">
                                <label class="custom-control-label" for="cstall">Check All</label>
                            </div>
                        </div>
                        
                    </div>
                    <!-- Action part -->
                    
                    <!-- Mail list-->
                    <div class="table-responsive">
                        <table class="table email-table no-wrap table-hover v-middle">
                            <thead>
                                <tr>
                                    <th scope="col">Sr No.</th>
                                    <th scope="col">Image</th>                                                
                                    <th scope="col">Farmer Name</th>
                                    <th scope="col">Query</th>
                                    <th scope="col">Status</th>
                                    <th scope="col">Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- row -->
                                {tr_html}
                                
                            </tbody>
                        </table>
                    </div>
                    <div class="p-15 m-t-30">
                        <nav aria-label="Page navigation example">
                            <ul class="pagination justify-content-center">
                                <li class="page-item"><a class="page-link" href="javascript:void(0)">Previous</a></li>
                                <li class="page-item"><a class="page-link" href="javascript:void(0)">1</a></li>
                                <li class="page-item"><a class="page-link" href="javascript:void(0)">2</a></li>
                                <li class="page-item"><a class="page-link" href="javascript:void(0)">3</a></li>
                                <li class="page-item"><a class="page-link" href="javascript:void(0)">Next</a></li>
                            </ul>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
         
""")
import footer