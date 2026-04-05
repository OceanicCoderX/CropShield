#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import sys
import cgi
import cgitb
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
PCId = form.getvalue("pcid")
DId = form.getvalue("did")

if DId:
   query = f"SELECT p.PId, pc.Name, d.Name, p.Name, p.Image, p.Detail, p.Usege FROM product p JOIN productcategory pc ON p.PCId = pc.PCId JOIN diseases d ON p.DId = d.DId WHERE p.DId={DId}"
   # print(query)
   mycursor.execute(query)
   myresult = mycursor.fetchall()
   # print(myresult)
else:
   query = f"SELECT p.PId, pc.Name, d.Name, p.Name, p.Image, p.Detail, p.Usege FROM product p JOIN productcategory pc ON p.PCId = pc.PCId JOIN diseases d ON p.DId = d.DId WHERE p.PCId={PCId}"
   # print(query)
   mycursor.execute(query)
   myresult = mycursor.fetchall()
   # print(myresult)

tr_html = ''
for x in myresult:
    tr_html += f'''
         <div class="col-lg-3 col-sm-6">
            <div class="product-box">
               <div class="pro-thumb"> <a href="details.py?pid={x[0]}"><i class="fa-solid fa-eye"></i></a> <img src="html/ltr/assets/Product/{x[0]}/{x[4]}" alt=""></div>
               <div class="pro-txt">
                  <h5><a href="details.py?pid={x[0]}"  style="color:black">{x[3]}</a></h5>
                  <b>Category : </b>{x[1]} <br>
                  <b>Desises : </b>{x[2]}
               </div>
            </div>
         </div>
'''

import header
print(f"""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1>Product</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#"> Shop </a></li>
                  <li><a href="#"> Products</a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End--> 
         
         <!--Contact Start-->
         <section class="shop wf100 p80">
            <div class="container">
               <div class="row">
               
                  <!--Pro Box Start-->
                  {tr_html}
                  <!--Pro Box End--> 
                  
               </div>
            </div>
         </section>
         <!--Contact End--> 
""")
import footer
