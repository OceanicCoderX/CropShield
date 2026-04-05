#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")

print("""
<!DOCTYPE html>
<html dir="ltr" lang="en">


<!-- Mirrored from themedesigner.in/demo/wrappixel/admin-template/xtreme/html/ltr/form-basic.html by HTTrack Website Copier/3.x [XR&CO'2014], Wed, 06 Jun 2018 05:49:08 GMT -->
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- Tell the browser to be responsive to screen width -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- Favicon icon -->
    <link rel="icon" type="image/png" sizes="16x16" href="../../assets/images/favicon.png">
    <title>CropShield Admin Panel</title>
    <!-- This Page CSS -->
    <link href="../../assets/libs/summernote/dist/summernote-bs4.css" rel="stylesheet">
    <link href="../../assets/libs/dropzone/dist/min/dropzone.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link href="../../dist/css/style.min.css" rel="stylesheet">
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <!--Fa Icons-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.0/css/all.min.css" integrity="sha512-DxV+EoADOkOygM4IR9yXP8Sb2qwgidEmeqAEmDKIOfPRQZOWbXCzLC6vjbZyy0vPisbH2SyW27+ddLVCN+OMzQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<![endif]-->

    <!-- DataTables Core CSS -->
    <link rel="stylesheet" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.min.css">

    <!-- Buttons Extension CSS -->
    <link rel="stylesheet" href="https://cdn.datatables.net/buttons/1.7.1/css/buttons.dataTables.min.css">
</head>

<body>
    <!-- ============================================================== -->
    <!-- Preloader - style you can find in spinners.css -->
    <!-- ============================================================== -->
    <div class="preloader">
        <div class="lds-ripple">
            <div class="lds-pos"></div>
            <div class="lds-pos"></div>
        </div>
    </div>
    <!-- ============================================================== -->
    <!-- Main wrapper - style you can find in pages.scss -->
    <!-- ============================================================== -->
    <div id="main-wrapper">
        <!-- ============================================================== -->
        <!-- Topbar header - style you can find in pages.scss -->
        <!-- ============================================================== -->
        <header class="topbar">
            <nav class="navbar top-navbar navbar-expand-md navbar-dark">
                <div class="navbar-header">
                    <!-- This is for the sidebar toggle which is visible on mobile only -->
                    <a class="nav-toggler waves-effect waves-light d-block d-md-none" href="javascript:void(0)"><i class="ti-menu ti-close"></i></a>
                    <!-- ============================================================== -->
                    <!-- Logo -->
                    <!-- ============================================================== -->
                    <a class="navbar-brand" href="index.html">
                        <!-- Logo text -->
                        <span class="logo-text">
                             <!-- Light Logo text -->    
                             <img src="../../assets/images/Crop_Shield_logo.png" class="light-logo" alt="homepage" style="width:200px; height:120px; margin-top: 15px; margin-bottom: -20px;"/>
                        </span>
                    </a>
                    <!-- ============================================================== -->
                    <!-- End Logo -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Toggle which is visible on mobile only -->
                    <!-- ============================================================== -->
                    <a class="topbartoggler d-block d-md-none waves-effect waves-light" href="javascript:void(0)" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><i class="ti-more"></i></a>
                </div>
                <!-- ============================================================== -->
                <!-- End Logo -->
                <!-- ============================================================== -->
                <div class="navbar-collapse collapse" id="navbarSupportedContent">
                    <!-- ============================================================== -->
                    <!-- toggle and nav items -->
                    <!-- ============================================================== -->
                    <ul class="navbar-nav float-left mr-auto">
                        <li class="nav-item d-none d-md-block"><a class="nav-link sidebartoggler waves-effect waves-light" href="javascript:void(0)" data-sidebartype="mini-sidebar"><i class="mdi mdi-menu font-24"></i></a></li>
                        <!-- ============================================================== -->
                        <!-- ============================================================== -->
                    </ul>
                    <!-- ============================================================== -->
                    <!-- Right side toggle and nav items -->
                    <!-- ============================================================== -->
                    <ul class="navbar-nav float-right">
                        <!-- Language selector -->
                        <li class="nav-item" style="margin-right:10px; margin-top:6px;">
                            <select id="langSelect" class="form-control" style="height:36px;">
                                <option value="en">English</option>
                                <option value="hi">à¤¹à¤¿à¤¨à¥à¤¦à¥€</option>
                                <option value="mr">à¤®à¤°à¤¾à¤ à¥€</option>
                            </select>
                        </li>

                        <!-- User profile and search -->
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle text-muted waves-effect waves-dark pro-pic" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><img src="../../assets/images/users/1.jpg" alt="user" class="rounded-circle" width="31"></a>
                            <div class="dropdown-menu dropdown-menu-right user-dd animated flipInY">
                                <span class="with-arrow"><span class="bg-primary"></span></span>
                                <div class="d-flex no-block align-items-center p-15 bg-primary text-white m-b-10">
                                    <div class=""><img src="../../assets/images/users/1.jpg" alt="user" class="img-circle" width="60"></div>
                                    <div class="m-l-10">
                                        <h4 class="m-b-0 AdminName"></h4>
                                        <p class=" m-b-0 Email"></p>
                                    </div>
                                </div>
                                <a class="dropdown-item" id="changepwd"><i class="ti-key m-r-5 m-l-5"></i> Change Password</a>
                                <div class="dropdown-divider"></div>
                                <a class="dropdown-item" href="LogOut.py"><i class="fa fa-power-off m-r-5 m-l-5"></i>Logout</a>
                                <div class="dropdown-divider"></div>
                            </div>
                        </li>
                    </ul>
                </div>
            </nav>
        </header>
        <!-- ============================================================== -->
        <!-- End Topbar header -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <aside class="left-sidebar">
            <!-- Sidebar scroll-->
            <div class="scroll-sidebar">
                <!-- Sidebar navigation-->
                <nav class="sidebar-nav">
                    <ul id="sidebarnav">
                        <!-- User Profile-->
                        <li>
                            <!-- User Profile-->
                            <div class="user-profile d-flex no-block dropdown m-t-20">
                                <div class="user-pic"><img src="../../assets/images/users/1.jpg" alt="users" class="rounded-circle" width="40" /></div>
                                <div class="user-content hide-menu m-l-10">
                                    <a href="javascript:void(0)" class="" id="Userdd" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        <h5 class="m-b-0 user-name font-medium AdminName"></h5>
                                        <span class="op-5 user-email Email"></span>
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="Userdd">
                                        <a class="dropdown-item" id="changepwd"><i class="ti-key m-r-5 m-l-5"></i> Change Password</a>
                                        <div class="dropdown-divider"></div>
                                        <a class="dropdown-item" href="LogOut.py"><i class="fa fa-power-off m-r-5 m-l-5"></i> Logout</a>
                                    </div>
                                </div>
                            </div>
                            <!-- End User Profile-->
                        </li>
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">Admin Pannal</span></li>
                        
                        <li class="sidebar-item"> <a href="Dashboard.py" class="sidebar-link waves-effect waves-dark" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Dashboard</span></a></li>
                        <li class="sidebar-item"> <a href="javascript:void(0)" class="sidebar-link has-arrow waves-effect waves-dark" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Company Details</span></a>
                            <ul aria-expanded="false" class="collapse  first-level">
                                <li class="sidebar-item"><a href="CompanyList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Company </span></a></li>
                            </ul>
                        </li>
                        <li class="sidebar-item"> <a href="javascript:void(0)" class="sidebar-link has-arrow waves-effect waves-dark" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Crop Category</span></a>
                            <ul aria-expanded="false" class="collapse  first-level">
                                <li class="sidebar-item"><a href="CropCategory.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Add Crop Category </span></a></li>
                                <li class="sidebar-item"><a href="CropCategoryList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Crop Category List </span></a></li>
                            </ul>
                        </li>
                        <li class="sidebar-item"> <a href="javascript:void(0)" class="sidebar-link has-arrow waves-effect waves-dark" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Crops</span></a>
                            <ul aria-expanded="false" class="collapse  first-level">
                                <li class="sidebar-item"><a href="Crops.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Add Crop </span></a></li>
                                <li class="sidebar-item"><a href="CropsList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Crop List </span></a></li>
                            </ul>
                        </li>
                        <li class="sidebar-item"> <a href="javascript:void(0)" class="sidebar-link has-arrow waves-effect waves-dark" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Crop Parts</span></a>
                            <ul aria-expanded="false" class="collapse  first-level">
                                <li class="sidebar-item"><a href="CropPart.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Add Crop Parts </span></a></li>
                                <li class="sidebar-item"><a href="CropPartList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Crop Parts List </span></a></li>
                            </ul>
                        </li>
                        <li class="sidebar-item"> <a href="javascript:void(0)" class="sidebar-link has-arrow waves-effect waves-dark" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Diseases</span></a>
                            <ul aria-expanded="false" class="collapse  first-level">
                                <li class="sidebar-item"><a href="Diseases.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Add Diseases </span></a></li>
                                <li class="sidebar-item"><a href="DiseasesList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Diseases List </span></a></li>
                            </ul>
                        </li>
                        <li class="sidebar-item"> <a href="javascript:void(0)" class="sidebar-link has-arrow waves-effect waves-dark" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Symptoms</span></a>
                            <ul aria-expanded="false" class="collapse  first-level">
                                <li class="sidebar-item"><a href="Symptoms.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Add Symptoms </span></a></li>
                                <li class="sidebar-item"><a href="SymptomsList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Symptoms List </span></a></li>
                            </ul>
                        </li>
                        <li class="sidebar-item"> <a href="javascript:void(0)" class="sidebar-link has-arrow waves-effect waves-dark" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Product Category</span></a>
                            <ul aria-expanded="false" class="collapse  first-level">
                                <li class="sidebar-item"><a href="Productcategory.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Add Product Category </span></a></li>
                                <li class="sidebar-item"><a href="ProductCategorylist.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Product Category List </span></a></li>
                            </ul>
                        </li>
                        <li class="sidebar-item"> <a href="javascript:void(0)" class="sidebar-link has-arrow waves-effect waves-dark" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Product</span></a>
                            <ul aria-expanded="false" class="collapse  first-level">
                                <li class="sidebar-item"><a href="Product.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Add Product </span></a></li>
                                <li class="sidebar-item"><a href="ProductList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Product List </span></a></li>
                            </ul>
                        </li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Farmer</span></a>
                            <ul aria-expanded="false" class="collapse first-level">
                                <li class="sidebar-item"><a href="FarmerList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Farmer List </span></a></li>
                                <li class="sidebar-item"><a class="has-arrow sidebar-link" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Farmer Query </span></a>
                                    <ul aria-expanded="false" class="collapse second-level" style="margin-left: 15px;">
                                        <li class="sidebar-item"><a href="FarmerQuery.py" class="sidebar-link"><i class="mdi mdi-octagram"></i><span class="hide-menu"> Farmers Query</span></a></li>
                                        <li class="sidebar-item"><a href="QueryList.py" class="sidebar-link"><i class="mdi mdi-octagram"></i><span class="hide-menu">Replayed Query List</span></a></li>
                                        <li class="sidebar-item"><a href="publicquery.py" class="sidebar-link"><i class="mdi mdi-octagram"></i><span class="hide-menu">Public Querys</span></a></li>
                                    </ul>
                                </li>
                                <li class="sidebar-item"><a href="FarmerFeedback.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu"> Farmer Feedback </span></a></li>
                            </ul>
                        </li>               
                    </ul>
                </nav>
                <!-- End Sidebar navigation -->
            </div>
            <!-- End Sidebar scroll-->
        </aside>
        <!-- ============================================================== -->
        <!-- End Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
""")


print("""
    <script>
        let AId = localStorage.getItem("AId");
        let AdminName = localStorage.getItem("AdminName");
        let PhoneNo = localStorage.getItem("PhoneNo");
        let Email = localStorage.getItem("Email");

        if (AdminName || AId || PhoneNo || Email) {
            document.querySelectorAll(".AdminName").forEach(el => {
                el.innerHTML = AdminName || "";
            });
            document.querySelectorAll(".Email").forEach(el => {
                el.innerHTML = Email || "";
            });

        } else {
            alert("âš ï¸ Please login first!");
            window.location.href = "adminlogin.py";
        }
        
        let changepwd = document.getElementById("changepwd");
			if(changepwd && Email) {
				changepwd.href = "ResetPassword.py?email=" + Email;
			}
    </script>

    <!-- Language script -->
    <script src="../../assets/js/lang.js"></script>

""")
