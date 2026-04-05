#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
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
               <h1>Login â€” CropShield</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#"> Login </a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End-->

         <section class="wf100 p80">
            <div class="container">
               <div class="row">
                  <div class="col-lg-6 offset-lg-3">
                     <div class="login-box">
                        <form action="loginBackEnd.py" id="loginForm" method="POST">
                           <h3>Login to your account</h3>
                            <div class="input-group">
                                <input type="tel" name="phone" id="phone" class="form-control" placeholder="Phone number" required>
                            </div>
                            <div class="input-group">
                                <input type="password" name="password" id="password" class="form-control" placeholder="Password" required>
                            </div>
                            <a href="#" id="forgotLink" style="float:right; color:#2b8a3e; font-weight:500; margin-top:-20px;">Forgot Password?</a><br><br>
                            <div class="input-group">
                                <button class="login-btn" type="submit" name="login" value="1">Login Account</button>
                            </div>
                        </form>

                        <div style="margin-top:10px;text-align:center;">
                           <p class="small-note">Don't have an account? <a href="register.py">Register here</a></p>
                        </div>

                        <form action="SendOTP.py" id="resetForm" style="display:none;margin-top:12px;" method="POST">
                           <h3>Password Recover</h3>
                           <div class="input-group">
                              <input type="email" name="Email" id="Email" class="form-control" placeholder="Enter your Email to reset">
                              <input type="tel" name="PhoneNo" id="PhoneNo" class="form-control" placeholder="Enter your Number to reset">
                           </div>
                           <div class="input-group">
                              <button class="login-btn" type="submit">Send Reset Password</button>
                           </div>
                        </form>

                     </div>
                  </div>
               </div>
            </div>
         </section>

         <script>
         document.addEventListener('DOMContentLoaded', function(){
            var forgot = document.getElementById('forgotLink');
            var reset = document.getElementById('resetForm');
            var login = document.getElementById('loginForm');
            if(forgot) forgot.addEventListener('click', function(e){ e.preventDefault(); login.style.display='none'; reset.style.display='block'; });
         });
         </script>

""")
import footer
