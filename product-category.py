#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
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

query = "SELECT * FROM productcategory"
mycursor.execute(query)
myresult = mycursor.fetchall()
# print(myresult)

tr_html = ''
for x in myresult:
   tr_html += f'''
            <div class="col-lg-6 col-md-6">
               <!--Project Box Start-->
               <div class="pro-list-box">
               <div class="pro-thumb"><img src="html/ltr/assets/ProductCategory/{x[0]}/{x[2]}" style="width:100%; height:250px;"> </div>
                  <div class="pro-txt">
                     <h3> <a href="product.py?pcid={x[0]}">{x[1]}</a> </h3>
                     <p> {x[3]} </p>
                     <a href="product.py?pcid={x[0]}" class="view">View Products</a> 
                  </div>
               </div> 
               <!--Project Box End-->  
            </div>
   '''

import header
print(f"""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1 data-i18n="prodcat_title">Products Category</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#">Pages </a></li>
                  <li><a href="#">Projects</a></li>
                  <li><a href="#">Projects List</a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End--> 
         <!--Causes Start-->
         <section class="wf100 p80 projects">
            <div class="projects-list">
               <div class="container">
                  <div class="row">
                     {tr_html}
                  </div>
               </div>
            </div>
         </section>
         <!--Causes End--> 

""")
import footer
