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

procduct = "SELECT p.PId, p.Image, p.Name, pc.PCId, pc.Name FROM product p JOIN productcategory pc ON p.PCId = pc.PCId;"
mycursor.execute(procduct)
myresult = mycursor.fetchmany(6)
# print(myresult)

pro_cat = ''
for x in myresult:
   pro_cat += f'''
      <li><a href="productpy?pcid={x[3]}">{x[4]}</a></li>
   '''

pro_Img = ''
for x in myresult:
   pro_Img += f'''
         <div class="item">
            <div class="f-product" style="height:300px">
               <img src="html/ltr/assets/Product/{x[0]}/{x[1]}" style="height:75%">
               <div class="fp-text">
                  <h6><a href="product.py">{x[2]}</a></h6>
               </div>
            </div>
         </div>
   '''

print(f"""
         <!--Footer Start-->
         <footer class="footer">
            <div class="footer-top wf100">
               <div class="container">
                  <div class="row">
                     <div class="col-lg-3 col-md-6 col-sm-6">
                        <!--Footer Widget Start-->
                        <div class="footer-widget">
                           <h4 data-i18n="footer_about_title">About CropShield</h4>
                           <p data-i18n="footer_about_text">We provide image-based guides, symptom checkers, and a direct farmer-to-admin connection so farmers receive timely, actionable advice. Our mission is to reduce yield loss and promote sustainable, affordable solutions for small and large farms alike.</p>
                           <a href="about.py" class="lm" data-i18n="footer_about_link">About us</a> 
                        </div>
                        <!--Footer Widget End--> 
                     </div>
                     <div class="col-lg-3 col-md-6 col-sm-6">
                        <!--Footer Widget Start-->
                        <div class="footer-widget">
                           <h4 data-i18n="footer_product_category">Product Category</h4>
                           <ul class="quick-links">
                           {pro_cat}
                           </ul>
                        </div>
                        <!--Footer Widget End--> 
                     </div>
                     <div class="col-lg-3 col-md-6 col-sm-6">
                        <!--Footer Widget Start-->
                        <div class="footer-widget">
                           <h4 data-i18n="footer_queries">Queries</h4>
                           <ul class="lastest-products">
                              <li> <strong><a href="faq.py"> How do I identify diseases in my crops? </a></strong> <span class="pdate"><i>Posted:</i> 29 September, 2018</span> </li>
                              <li> <strong><a href="faq.py"> What preventive measures can I take to protect crops? </a></strong> <span class="pdate"><i>Posted:</i> 29 September, 2018</span> </li>
                              <li> <strong><a href="faq.py"> Can I upload images for diagnosis? </a></strong> <span class="pdate"><i>Posted:</i> 29 September, 2018</span> </li>
                           </ul>
                        </div>
                        <!--Footer Widget End--> 
                     </div>
                     <div class="col-lg-3 col-md-6 col-sm-6">
                        <!--Footer Widget Start-->
                        <div class="footer-widget">
                           <div id="fpro-slider" class="owl-carousel owl-theme">
                           
                              <!--Footer Product Start-->
                              {pro_Img}
                              <!--Footer Product End--> 
                               
                           </div>
                        </div>
                        <!--Footer Widget End--> 
                     </div>
                  </div>
               </div>
            </div>
            <div class="footer-copyr wf100">
               <div class="container">
                  <div class="row">
                     <div class="col-md-4 col-sm-4"> <img src="images/Crop_Shield.png" alt=""> </div>
                  </div>
               </div>
            </div>
         </footer>
         <!--Footer End--> 
      </div>
""")
print("""
      <!--   JS Files Start  --> 
      <script src="js/jquery-3.3.1.min.js"></script> 
      <script src="js/jquery-migrate-1.4.1.min.js"></script> 
      <script src="js/popper.min.js"></script> 
      <script src="js/bootstrap.min.js"></script> 
      <script src="js/owl.carousel.min.js"></script> 
      <script src="js/jquery.prettyPhoto.js"></script> 
      <script src="js/isotope.min.js"></script> 
      <script src="js/custom.js"></script>
         <!-- Inline script to create mobile bottom nav (page-local) -->
         <script>
         (function(){
            function buildMobileNav(){
               if(document.querySelector('.mobile-bottom-nav')) return;
               if(window.innerWidth>768) return;
               var items = [
                  {i18n:'mobile_home', label:'Home', href:'index.py', icon:'fa-solid fa-house'},
                  {i18n:'mobile_products', label:'Products', href:'projects.html', icon:'fa-solid fa-boxes-stacked'},
                  {i18n:'mobile_cropcategory', label:'CropCategory', href:'crop-category.py', icon:'fa-solid fa-seedling'},
                  {i18n:'mobile_faq', label:'FAQ', href:'faq.py', icon:'fa-solid fa-file'},
                  {i18n:'mobile_dashboard', label:'Dashboard', href:'dashboard.py',  icon:'fa fa-tachometer-alt'}
               ];
               var nav = document.createElement('nav'); nav.className='mobile-bottom-nav'; nav.setAttribute('aria-label','Mobile bottom navigation');
               items.forEach(function(it){
                  var a = document.createElement('a'); a.href = it.href;
                  a.className = 'mbn-link';
                  var icon = document.createElement('span'); icon.className='mbn-icon';
                  var iTag = document.createElement('i'); iTag.className = it.icon; icon.appendChild(iTag);
                  var label = document.createElement('span'); label.className='mbn-label'; label.textContent = it.label;
                  if(it.i18n) label.setAttribute('data-i18n', it.i18n);
                  a.appendChild(icon); a.appendChild(label);
                  if(it.isCart){
                     a.addEventListener('click', function(e){
                        e.preventDefault();
                        // attempt to trigger bootstrap dropdown if present
                        var cartBtn = document.getElementById('cartdropdown');
                        if(cartBtn){
                           // using Bootstrap dropdown toggle
                           if(typeof jQuery !== 'undefined') jQuery(cartBtn).dropdown('toggle');
                           else {
                              // fallback: toggle visibility of dropdown menu
                              var menu = cartBtn.nextElementSibling;
                              if(menu) menu.classList.toggle('show');
                           }
                        } else {
                           window.location.href = it.href;
                        }
                     });
                  }
                  nav.appendChild(a);
               });
               document.body.appendChild(nav);
               // if lang loader is present, re-apply translations to dynamically created items
               try{ if(window.setLanguage) window.setLanguage(localStorage.getItem('lang') || 'en'); }catch(e){}
            }
            // build on load and on resize (debounced)
            function onResize(){ clearTimeout(window._mbnav_t); window._mbnav_t = setTimeout(buildMobileNav,120); }
            window.addEventListener('load', buildMobileNav);
            window.addEventListener('resize', onResize);
         })();
         </script>
         
         <!--Important js for animation-->
         <script type="text/javascript" src="js/wow.js"></script>
         <script>
                  new WOW().init();
         </script>
                  
         <script>
            let FId = localStorage.getItem("FId");
            console.log(FId)
            let FName = localStorage.getItem("FName");
            let PhoneNo = localStorage.getItem("PhoneNo");
            let Email = localStorage.getItem("Email");

            if (FName || FId || PhoneNo || Email) {
               document.querySelectorAll(".FName").forEach(el => {
                  el.innerHTML = FName || "";
               });
               document.querySelectorAll(".Email").forEach(el => {
                  el.innerHTML = Email || "";
               });

            } else {
               document.querySelectorAll(".FName").forEach(el => {
                  el.innerHTML = "Guest";
               });
            }

            <!--- Link to a tag -->

            let faqLink = document.getElementById("faqLink");
            console.log(faqLink)
            console.log(FId)
            if(faqLink && FId) {
               faqLink.href = "faq.py?fid=" + FId;
            }

            let dashboardLink = document.getElementById("dashboardLink");
            console.log(dashboardLink)
            console.log(FId)
            if(dashboardLink && FId) {
               dashboardLink.href = "dashboard.py?fid=" + FId;
            }


            <!--- Link to a button -->

            document.addEventListener('DOMContentLoaded', function() {
               document.querySelectorAll('.add-to-wishlist').forEach(function(btn) {
                  btn.addEventListener('click', function() {
                  var pid = btn.getAttribute('data-pid');
                  var uid = localStorage.getItem('Id');
                  window.location.href = 'wishlist.py?pid=' + encodeURIComponent(pid) + '&uid=' + encodeURIComponent(uid);
                  });
               });
            });

         </script>


   </body>

</html>
""")
