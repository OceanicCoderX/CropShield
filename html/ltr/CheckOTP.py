#!C:/Python310/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-Type:text/html\n")

form = cgi.FieldStorage()
Email = form.getvalue("email")
otp = form.getvalue("otp")

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
query = f""" SELECT * FROM adminlogin WHERE Email = '{Email}'"""
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchone()
# print(myresult)

if(myresult):
    print("""
    <!DOCTYPE html>
    <html dir="ltr">


    <!-- Mirrored from themedesigner.in/demo/wrappixel/admin-template/xtreme/html/ltr/authentication-login1.html by HTTrack Website Copier/3.x [XR&CO'2014], Wed, 06 Jun 2018 05:51:50 GMT -->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <!-- Tell the browser to be responsive to screen width -->
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">
        <!-- Favicon icon -->
        <link rel="icon" type="image/png" sizes="16x16" href="../../assets/images/favicon.png">
        <title>Xtreme admin Template - The Ultimate Multipurpose admin template</title>
        <!-- Custom CSS -->
        <link href="../../dist/css/style.min.css" rel="stylesheet">
        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
    </head>

    <body>
        <div class="main-wrapper">
            <!-- ============================================================== -->
            <!-- Login box.scss -->
            <!-- ============================================================== -->
            <div class="auth-wrapper d-flex no-block justify-content-center align-items-center" style="background:url(../../assets/images/big/auth-bg.jpg) no-repeat center center;">
                <div class="auth-box">
                    <div id="loginform">
                        <div class="logo">
                            <span class="db"><img src="assets/AdminFile/logo.png" alt="logo" style="width:150px;" /></span>
                            <h5 class="font-medium m-b-20">Reset Password</h5>
                        </div>
    """)
    print(f"""      
                        <!-- Form -->
                        <div class="row">
                            <div class="col-12">
                                <form class="form-horizontal m-t-20" id="loginform" action="CheckOTPBackEnd.py" method="POST">
                                    <div class="input-group mb-3">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text" id="basic-addon1"><i class="ti-user"></i></span>
                                        </div>
                                        <input type="Email" class="form-control form-control-lg" placeholder="Email" aria-label="Email" name="Email" id="Email" aria-describedby="basic-addon1" value="{myresult[3]}" readonly>
                                    </div>
                                    <div class="input-group mb-3">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text" id="basic-addon2"><i class="ti-pencil"></i></span>
                                        </div>
                                        <input type="text id ="notp" name="notp" value="{otp}" hidden>
                                        <input type="text" class="form-control form-control-lg" placeholder=" Enter OTP" aria-label="Password" name="otp" id="otp" aria-describedby="basic-addon1">
                                    </div>
                                    <div class="form-group text-center">
                                        <div class="col-xs-12 p-b-20">
                                            <button class="btn btn-block btn-lg btn-danger" type="submit">Send OTP</button>
                                        </div>
                                    </div>
                                </form>
                                
    """)
    print("""  
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
            <!-- ============================================================== -->
            <!-- Login box.scss -->
            <!-- ============================================================== -->
        </div>
        <!-- ============================================================== -->
        <!-- All Required js -->
        <!-- ============================================================== -->
        <script src="../../assets/libs/jquery/dist/jquery.min.js"></script>
        <!-- Bootstrap tether Core JavaScript -->
        <script src="../../assets/libs/popper.js/dist/umd/popper.min.js"></script>
        <script src="../../assets/libs/bootstrap/dist/js/bootstrap.min.js"></script>
        <!-- ============================================================== -->
        <!-- This page plugin js -->
        <!-- ============================================================== -->
        <script>
        $('[data-toggle="tooltip"]').tooltip();
        $(".preloader").fadeOut();
        // ============================================================== 
        // Login and Recover Password 
        // ============================================================== 
        $('#to-recover').on("click", function() {
            $("#loginform").slideUp();
            $("#recoverform").fadeIn();
        });
        </script>
    </body>


    <!-- Mirrored from themedesigner.in/demo/wrappixel/admin-template/xtreme/html/ltr/authentication-login1.html by HTTrack Website Copier/3.x [XR&CO'2014], Wed, 06 Jun 2018 05:51:51 GMT -->
    </html>
        """)

else:
    print(f'''
    <script>alert("Invalid Email!");
    location.href="AdminLogin.py";
    </script>''')