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

print("""
<!doctype html>
<html lang="en">
   
<head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <meta name="description" content="">
      <meta name="author" content="">
      <link rel="icon" href="images/favicon.png">
      <title>Crop Shield</title>
      <!-- CSS FILES START -->
      <link href="css/custom.css" rel="stylesheet">
      <link href="css/color.css" rel="stylesheet">
      <link href="css/responsive.css" rel="stylesheet">
      <link href="css/owl.carousel.min.css" rel="stylesheet">
      <link href="css/bootstrap.min.css" rel="stylesheet">
      <link href="css/prettyPhoto.css" rel="stylesheet">
      <link href="css/all.min.css" rel="stylesheet">
      <link href="css/animate.css" rel="stylesheet">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
      <!-- CSS FILES End -->
         <!-- Inline mobile bottom nav styles (only for this page) -->
         <style>
         /* hidden by default; visible only on small screens */
         .mobile-bottom-nav{display:none}
         @media (max-width:767.98px){
            .mobile-bottom-nav{display:flex;position:fixed;left:0;right:0;bottom:0;height:60px;background:#fff;border-top:1px solid rgba(0,0,0,.08);box-shadow:0 -6px 18px rgba(0,0,0,.06);z-index:9999;align-items:center;justify-content:space-around;padding:6px 8px}
            .mobile-bottom-nav a{color:#2b8a3e;text-decoration:none;font-size:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;width:64px;height:48px}
            .mobile-bottom-nav .mbn-icon{width:40px;height:40px;border-radius:50%;background:#f0f7f1;display:flex;align-items:center;justify-content:center;margin-bottom:3px;font-size:18px;color:#2b8a3e}
            .mobile-bottom-nav .mbn-label{font-size:11px;color:#4a4a4a;line-height:1}
            body{padding-bottom:72px}
         }
         .language-icon{
               border: 1px solid #64b868;
               width: 34px;
               height: 34px;
               display: block;
               border-radius: 100%;
               text-align: center;
               line-height: 20px;
               color: #c8e6c9;
               font-size: 14px;
               margin: 5px 0 0;
         }
         </style>
   </head>
   <body>
      <div class="wrapper home2">
         <!--Header Start-->
         <header class="header-style-2">
            <nav class="navbar navbar-expand-lg">
               <a class="navbar-brand" href="index-2.html"><img src="images/Crop_Shield_logo.png" style="width:200px; height:150px; margin-top:-30px; margin-bottom:-30px;"></a>
               <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"> <i class="fas fa-bars"></i> </button>
               <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav mr-auto">
                     <li class="nav-item"> <a class="nav-link" href="index.py" data-i18n="nav_home">Home</a> </li>
                     <li class="nav-item"> <a class="nav-link" href="about.py" data-i18n="nav_about">About</a> </li>
                     <li class="nav-item"> <a class="nav-link" href="crop-category.py" data-i18n="nav_crops">Crops</a> </li>
                     <li class="nav-item"> <a class="nav-link" href="product-category.py" data-i18n="nav_products">Products</a> </li>
                     <li class="nav-item"> <a class="nav-link" href="contact.py" data-i18n="nav_contact">Contact</a> </li>
                     <li class="nav-item"> <a class="nav-link" href="testimonials.py" data-i18n="nav_testimonials">Testimonials</a> </li>
                  </ul>
                  
                  <ul class="topnav-right">
                     <li> <a class="mdonate" id="faqLink" href="faq.py"><span data-i18n="nav_faq">Farmer Ask Query</span></a> </li>
                     <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle language-icon" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                           <i class="fa-solid fa-language" style="margin-left:-7px;"></i>
                        </a>
                        <div class="dropdown-menu" aria-labelledby="langDropdown">
                           <a class="dropdown-item" href="javascript:void(0);" onclick="setLanguage('en')">English</a>
                           <a class="dropdown-item" href="javascript:void(0);" onclick="setLanguage('hi')">à¤¹à¤¿à¤¨à¥à¤¦à¥€ </a>
                           <a class="dropdown-item" href="javascript:void(0);" onclick="setLanguage('mr')">à¤®à¤°à¤¾à¤ à¥€</a>
                        </div>
                     </li>

                     <li> <a class="search-icon" href="#search"> <i class="fas fa-search"></i> </a> </li>
                     <li> <a class="cart-icon" id="dashboardLink" href="dashboard.py" > <i class="fa fa-tachometer-alt"></i></a></li>
""")
print("""
      <script>
         if(localStorage.getItem("FName")){
            var fid = localStorage.getItem("FId") || "";
            // include data-i18n on logout anchor so it can be translated
            document.write('<li class="login-reg"> <a href="myaccount.py?fid=' + fid + '" class="FName"></a> | <a href="logout.py" data-i18n="nav_logout">LogOut</a> </li>');
         }
         else{
            // add data-i18n attributes for login/signup so translations apply
            document.write('<li class="login-reg"> <a href="login.py" data-i18n="nav_login">Login</a> | <a href="register.py" data-i18n="nav_signup">Signup</a> </li>');         
         }
      </script>
""")
print("""
                  </ul>
               </div>
            </nav>
         </header>
         <div id="search">
            <button type="button" class="close">Ã—</button>
            <form class="search-overlay-form">
               <input type="search" value="" placeholder="type keyword(s) here" />
               <button type="submit" class="btn btn-primary"><i class="fas fa-search"></i></button>
            </form>
         </div>
      <!--Header End--> 
         
         
""")
print('<script src="assets/js/lang.js"></script>')
