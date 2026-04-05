#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
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
query = "SELECT * FROM productcategory"
mycursor.execute(query)
myresult = mycursor.fetchall()
# print(myresult)

import header
print(f"""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1 data-i18n="prod_title">Solar & Wind Energies</h1>
               <ul>
                  <li><a href="#" data-i18n="nav_home">Home</a></li>
                  <li><a href="#" data-i18n="nav_products"> Shop </a></li>
                  <li><a href="#" data-i18n="prod_breadcrumb_item">Premium Woo Shirt</a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End--> 
         <!--Blog Start-->
         <section class="wf100 p80 shop">
            <div class="product-details">
               <div class="container">
                  <div class="row">
                     <div class="col-md-6">
                        <div class="pro-large"><img src="images/shoplarge.jpg" alt=""></div>
                     </div>
                     <div class="col-md-6">
                        <div class="product-text">
                           <h2 data-i18n="prod_heading">Premium Woo Shirt</h2>
                           <div class="pro-rating"> <a href="#"><i class="fas fa-star"></i> <i class="fas fa-star"></i> <i class="fas fa-star"></i> <i class="fas fa-star"></i> <i class="fas fa-star-half-alt"></i></a> </div>
                           <div class="pro-pricing"><del>$25.00</del> $19.00 </div>
                           <p> We are going to run a solid educational campaign for the orphan children study. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum.</p>
                           <p>You need to be sure there isn't anything embarrassing hidden in the middle of text. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage. </p>
                           <div class="add-2-cart"> <strong>Quantity:</strong>
                              <input type="number" name="quantity" min="1" max="99">
                              <input type="submit" value="Add to Cart" name="Add to Cart">
                           </div>
                        </div>
                     </div>
                  </div>
                  <div class="row">
                     <div class="col-md-12">
                        <div class="products-tabs wf100 p80">
                           <nav>
                              <div class="nav nav-tabs" id="nav-tab" role="tablist"> <a class="nav-item nav-link active" id="nav-one-tab" data-toggle="tab" href="#nav-one" role="tab" aria-controls="nav-one" aria-selected="true" data-i18n="tab_description">Description</a> <a class="nav-item nav-link" id="nav-two-tab" data-toggle="tab" href="#nav-two" role="tab" aria-controls="#nav-two" aria-selected="true" data-i18n="tab_additional_info">Additional Information</a> <a class="nav-item nav-link" id="nav-three-tab" data-toggle="tab" href="#nav-three" role="tab" aria-controls="nav-three" aria-selected="false" data-i18n="tab_reviews">Reviews</a> </div>
                           </nav>
                           <div class="tab-content" id="nav-tabContent">
                              <div class="tab-pane fade show active" id="nav-one" role="tabpanel" aria-labelledby="nav-one-tab">
                                 <p> We are going to run a solid educational campaign for the orphan children study. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum. </p>
                                 <p>You need to be sure there isn't anything embarrassing hidden in the middle of text. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage. </p>
                              </div>
                              <div class="tab-pane fade" id="nav-two" role="tabpanel" aria-labelledby="nav-two-tab">
                                 <table>
                                    <tr>
                                       <td>Weight</td>
                                       <td>130 gm</td>
                                    </tr>
                                    <tr>
                                       <td>Dimensions</td>
                                       <td>70 x 40 x 50 cm</td>
                                    </tr>
                                    <tr>
                                       <td>Small</td>
                                       <td>Mauris consequat odio turpis, sed ultricies libero tincidunt i</td>
                                    </tr>
                                    <tr>
                                       <td>Large</td>
                                       <td>Condimentum nisi vitae, consequat libero integer sit amet velit neque. </td>
                                    </tr>
                                 </table>
                              </div>
                              <div class="tab-pane fade" id="nav-three" role="tabpanel" aria-labelledby="nav-three-tab">
                                 <ul class="comments">
                                    <!--Comment Start-->
                                    <li class="comment">
                                       <div class="user-thumb"> <img src="images/auser.jpg" alt=""></div>
                                       <div class="comment-txt">
                                          <h6> Mason Gray </h6>
                                          <p> Personally I think a combination of all these methods is most effective, but in todayâ€™s post I will be focusing specifically on how to use and style WordPressâ€™ built-in sticky post feature and highlighting itâ€™s best use case based on my own experience. </p>
                                          <ul class="comment-time">
                                             <li>Posted: 09 July, 2018 at 2:37 pm</li>
                                             <li> <a href="#"><i class="fas fa-reply"></i> Reply</a> </li>
                                          </ul>
                                       </div>
                                       <ul class="children">
                                          <!--Comment Start-->
                                          <li class="comment">
                                             <div class="user-thumb"> <img src="images/auser.jpg" alt=""></div>
                                             <div class="comment-txt">
                                                <h6> Rog Kelly </h6>
                                                <p> Personally I think a combination of all these methods is most effective, but in todayâ€™s post I will be focusing specifically on how to use and style WordPressâ€™ built-in sticky post feature and highlighting itâ€™s best use case based on my own experience. </p>
                                                <ul class="comment-time">
                                                   <li>Posted: 09 July, 2018 at 2:37 pm</li>
                                                   <li> <a href="#"><i class="fas fa-reply"></i> Reply</a> </li>
                                                </ul>
                                             </div>
                                          </li>
                                          <!--Comment End-->
                                       </ul>
                                    </li>
                                    <!--Comment End--> 
                                    <!--Comment Start-->
                                    <li class="comment">
                                       <div class="user-thumb"> <img src="images/auser.jpg" alt=""></div>
                                       <div class="comment-txt">
                                          <h6> Harry Butler </h6>
                                          <p> Personally I think a combination of all these methods is most effective, but in todayâ€™s post I will be focusing specifically on how to use and style WordPressâ€™ built-in sticky post feature and highlighting itâ€™s best use case based on my own experience. </p>
                                          <ul class="comment-time">
                                             <li>Posted: 09 July, 2018 at 2:37 pm</li>
                                             <li> <a href="#"><i class="fas fa-reply"></i> Reply</a> </li>
                                          </ul>
                                       </div>
                                    </li>
                                    <!--Comment End-->
                                 </ul>
                                 <div class="wf100 comment-form">
                                    <h4 data-i18n="leave_review">Leave a Review</h4>
                                    <p class="comment-notes"><span id="email-notes" data-i18n="your_email_note">Your email address will not be published.</span> Required fields are marked <span class="required">*</span></p>
                                    <div class="comment-form-rating">
                                       <label>Your rating</label>
                                       <p class="stars"><span><a class="star-1" href="#">1</a><a class="star-2" href="#">2</a><a class="star-3" href="#">3</a><a class="star-4" href="#">4</a><a class="star-5" href="#">5</a></span></p>
                                    </div>
                                    <ul>
                                       <li class="w3">
                                          <input type="text" class="form-control" placeholder="Full Name" data-i18n-placeholder="ph_full_name">
                                       </li>
                                       <li class="w3">
                                          <input type="text" class="form-control" placeholder="Email" data-i18n-placeholder="ph_email">
                                       </li>
                                       <li class="w3 np">
                                          <input type="text" class="form-control" placeholder="Subject" data-i18n-placeholder="ph_subject">
                                       </li>
                                       <li class="full">
                                          <textarea class="form-control" placeholder="Write Comments" data-i18n-placeholder="ph_write_comments"></textarea>
                                       </li>
                                       <li class="full">
                                          <button class="post-btn" data-i18n-value="btn_post_review">Post Your Review</button>
                                       </li>
                                    </ul>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
            <section class="online-shop wf100">
               <div class="container">
                  <div class="row">
            <div class="col-md-12">
               <h2 data-i18n="related_products">Related Products</h2>
                     </div>
                  </div>
                  <div class="row">
                     <!--Pro Box Start-->
                     <div class="col-md-3 col-sm-6">
                           <div class="product-box">
                           <div class="pro-thumb"> <a href="#" data-i18n-value="btn_add_to_cart">Add To Cart</a> <img src="images/pro1.jpg" alt=""></div>
                           <div class="pro-txt">
                              <h6><a href="#" data-i18n="prod_name_1">Happy Ninja Shirt</a></h6>
                              <p class="pro-price"><del>$25.00</del> $19.00</p>
                           </div>
                        </div>
                     </div>
                     <!--Pro Box End--> 
                     <!--Pro Box Start-->
                     <div class="col-md-3 col-sm-6">
                           <div class="product-box">
                           <div class="pro-thumb"> <a href="#" data-i18n-value="btn_add_to_cart">Add To Cart</a> <img src="images/pro2.jpg" alt=""></div>
                           <div class="pro-txt">
                              <h6><a href="#" data-i18n="prod_name_2">Woo corlor shirt</a></h6>
                              <p class="pro-price"><del>$25.00</del> $19.00</p>
                           </div>
                        </div>
                     </div>
                     <!--Pro Box End--> 
                     <!--Pro Box Start-->
                     <div class="col-md-3 col-sm-6">
                           <div class="product-box">
                           <div class="pro-thumb"> <a href="#" data-i18n-value="btn_add_to_cart">Add To Cart</a> <img src="images/pro3.jpg" alt=""></div>
                           <div class="pro-txt">
                              <h6><a href="#" data-i18n="prod_name_3">Premium Quality</a></h6>
                              <p class="pro-price"><del>$25.00</del> $19.00</p>
                           </div>
                        </div>
                     </div>
                     <!--Pro Box End--> 
                     <!--Pro Box Start-->
                     <div class="col-md-3 col-sm-6">
                           <div class="product-box">
                           <div class="pro-thumb"> <a href="#" data-i18n-value="btn_add_to_cart">Add To Cart</a> <img src="images/pro4.jpg" alt=""></div>
                           <div class="pro-txt">
                              <h6><a href="#" data-i18n="prod_name_4">Ninja Silhouette</a></h6>
                              <p class="pro-price"><del>$25.00</del> $19.00</p>
                           </div>
                        </div>
                     </div>
                     <!--Pro Box End--> 
                  </div>
               </div>
            </section>
         </section>
         <!--Blog End--> 

""")    
import footer
