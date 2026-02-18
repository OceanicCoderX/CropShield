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

query = "SELECT rq.RQId, rq.FQId, rq.Question, rq.Answer, rq.Position, rq.SuggestProduct, fq.QueryStatus FROM replayquery rq JOIN farmerquery fq ON rq.FQId = fq.FQId "
mycursor.execute(query)
myresult = mycursor.fetchall()
# print(myresult)

tr_html = ''
for x in myresult:
    rqid, fqid, que, ans, position, sugproduct, querystatus = x
    
    btn_class = 'btn-success' if position == 'public' else 'btn-secondary'
    btn_label = 'Public' if position == 'public' else 'Private'
    
    tr_html += f'''
    <tr>
        <td>{rqid}</td>
        <td><h5 class="mt-0 mb-1">{que}</h5> 
            {(ans[:100] + '...') if ans and len(ans)>100 else (ans or '')}
        </td>
        <td>
            <form action="queryposition.py" method="POST" style="display:inline-block;">
                <input type="hidden" name="fqid" id="fqid" value="{fqid}">
                <input type="hidden" name="status" id="status" value="{querystatus}">
                <input type="hidden" name="pos" id="pos" value="{position}">
                <button type="submit" class="btn {btn_class} btn-sm">{btn_label}</button>
            </form>
        </td>
        <td><a href="QueryDelete.py?qid={rqid}" onclick="return confirm('Are you sure to delete?')"><i class="fa-solid fa-trash"></i></a>
            <a href="QueryReplayEdit.py?qid={fqid}"><i class="fa-solid fa-pen-to-square"></i></a>
        </td>
    </tr>
    '''
    
import header
print(f"""
        <div class="page-wrapper">
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Farmer Query List</h4>
                    </div>   
                </div>
            </div>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr>
                                                <th scope="col">Sr No.</th>
                                                <th scope="col">Query</th>
                                                <th scope="col">Position</th>
                                                <th scope="col">Action</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {tr_html}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                <!-- ============================================================== -->
                <!-- End PAge Content -->
                <!-- ============================================================== -->
            </div>
            <!-- ============================================================== -->
            <!-- End Container fluid  -->
            <!-- ============================================================== -->
""")
import footer
