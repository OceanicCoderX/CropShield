#!C:/Python310/python.exe
import sys
import cgi
import cgitb
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
# print("Content-Type:text/html; charset=utf-8\n")

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

import header
print("""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1>Register — CropShield</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#"> Register </a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End-->

         <section class="wf100 p80">
            <div class="container">
               <div class="row">
                  <div class="col-lg-8 offset-lg-2">
                     <div class="myaccount-form">
                        <h3>Create a Farmer Account</h3>
                        
                        <form action="registerBackEnd.py" method="post">
                           <ul class="row cform">
                              <li class="col-md-6 half pr-15">
                                 <div class="input-group">
                                    <input type="text" name="name" id="name" class="form-control" placeholder="Farmer name" required>
                                 </div>
                              </li>
                              <li class="col-md-6 half pl-15">
                                 <div class="input-group">
                                    <input type="email" name="email" id="email"class="form-control" placeholder="Email address" required>
                                 </div>
                              </li>
                              <li class="col-md-6 half pr-15">
                                 <div class="input-group">
                                    <input type="tel" name="phone" id="phone" class="form-control" placeholder="Phone number" required>
                                 </div>
                              </li>
                              <li class="col-md-6 half pl-15">
                                 <div class="input-group">
                                    <input type="password" name="password" id="password" class="form-control" placeholder="Password" required>
                                 </div>
                              </li>
                              <li class="col-md-12 full">
                                 <div class="input-group">
                                    <input type="text" name="address" id="address" class="form-control" placeholder="Address" required>
                                 </div>
                              </li>
                              <li class="col-md-6 half pr-15">
                                 <div class="input-group">
                                    <input type="text" name="district" id="district" class="form-control" placeholder="District" required>
                                 </div>
                              </li>
                              <li class="col-md-6 half pl-15">
                                 <div class="input-group">
                                    <input type="text" name="state" id="state" class="form-control" placeholder="State" required>
                                 </div>
                              </li>
                              <li class="col-md-12 full">
                                 <div class="input-group form-check">
                                    <input type="checkbox" class="form-check-input" id="terms" required>
                                    <label class="form-check-label" for="terms">I agree to the Terms of Services & Privacy Policy</label>
                                 </div>
                              </li>
                              <button type="submit" name="register" class="register fsubmit">Register Your Account</button>
                              
                           </ul>
                        </form>
                        <div style="margin-top:12px;text-align:center;">
                           <p class="small-note">Already have an account? <a href="login.py">Login here</a></p>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </section>

""")
import footer
