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
PId = form.getvalue("pid")

query = f"""SELECT p.PId, pc.Name, d.Name, p.Name, p.Image, p.Detail, p.Usege FROM product p JOIN productcategory pc ON p.PCId = pc.PCId JOIN diseases d ON p.DId = d.DId WHERE p.PId={PId}"""
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchone()
# print(myresult)

import header
print(f"""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1>Product Detail Page</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#"> Team </a></li>
                  <li><a href="#">{myresult[1]}</a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End--> 
         <!--Blog Start-->
         <section class="wf100 p80 team">
            <div class="team-details">
               <div class="container">
                  <div class="row">
                     <div class="col-md-5">
                        <div class="team-large-img"> <img src="html/ltr/assets/Product/{myresult[0]}/{myresult[4]}" alt=""> </div>
                     </div>
                     <div class="col-md-7">
                        <div class="team-details-txt">
                           <h2>{myresult[2]}</h2>
                           <b>Category : </b>{myresult[1]} <br>
                           <b>Product Name : </b>{myresult[3]} <br><br>
                           <h4>Product Details</h4>
                           <p>{myresult[5]}</p>
                           <h4>How to use?</h4>
                           <p>{myresult[6]}</p> 
                        </div>
                     </div>
                  </div>
               </div>
            </div>
            
         </section>
         <!--Blog End--> 
         
""")
import footer