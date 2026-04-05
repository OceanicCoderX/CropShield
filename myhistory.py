#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import sys
import cgi
import cgitb
import mysql.connector
from connect import *
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

form = cgi.FieldStorage()
FId = form.getvalue("fid")

fquery = f"""SELECT fq.FQId, fq.FId, c.CropName , p.Name , fq.Date, fq.SymptomsDetails, 
            fq.SImg, fq.QueryStatus FROM farmerquery fq JOIN crops c ON fq.CropName = c.CropId 
            JOIN parts p ON fq.PartName = p.PartId 
            WHERE fq.FId = {FId};"""
# print(fquery)
mycursor.execute(fquery)
myresult = mycursor.fetchall()

if myresult:
    history = ''
    for x in myresult:
        history += f"""

            <!-- Query 1 - Replied -->
            <div class="query-card">
                <div class="query-header">
                    <div class="query-title">{x[2]} {x[3]} Disease</div>
                    <span class="status-badge {'status-replied' if x[7] == 'Replied' else 'status-pending'}">{x[7]}</span>
                </div>

                <div class="query-details">
                    <div class="detail-item">
                        <div class="detail-label">Crop Name</div>
                        <div class="detail-value">{x[2]}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Crop Part</div>
                        <div class="detail-value">{x[3]}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Query Date</div>
                        <div class="detail-value">{x[4]}</div>
                    </div>
                </div>

                <div class="symptoms-section">
                    <div class="symptoms-label">Symptoms</div>
                    <div class="symptoms-text">{x[5]}</div>
                </div>

                <div class="images-section">
                    <div class="images-label">Uploaded Images</div>
                    <div class="images-grid">
                        <img src="html/ltr/assets/FqueryImg/{x[0]}/{x[6]}" alt="Tomato leaf disease" class="image-thumbnail">
                    </div>
                </div> 
                <button class="filter-btn active" style="float:right; margin:20px; padding:10px; width:150px;" onclick="window.location.href='deletequery.py?fqid={x[0]}&fid={x[1]}'"> <b style="color:White">Delete</b> </button>   
        """

        # Fetch admin reply for THIS query (FQId = x[0])
        mycursor.execute(f"SELECT rq.Question, rq.Answer, rq.SuggestProduct, p.Image, p.Name, p.Usege FROM replayquery rq JOIN product p ON rq.SuggestProduct = p.PId WHERE rq.FQId = {myresult[0][0]} ORDER BY rq.RQId DESC;")
        reply = mycursor.fetchone()

        if x[7] == 'Replied' and reply:
            history += f"""
                <!-- Admin Response -->
                <div class="admin-response">
                    <div class="admin-response-title">Admin Response</div>

                    <div class="response-item">
                        <div class="response-label">Question</div>
                        <div class="response-content">{reply[0]}</div>
                    </div>

                    <div class="response-item">
                        <div class="response-label">Answer & Diagnosis</div>
                        <div class="response-content">{reply[1]}</div>
                    </div>

                    <div class="response-item">
                        <div class="response-label">Suggested Product</div>
                        <div class="suggested-product">
                            <img src="html/ltr/assets/Product/{reply[2]}/{reply[3]}" alt="Tomato leaf disease" style="width:150px; height:150px;">
                            <div class="product-name">ðŸŒ¿{reply[4]}</div>
                            <div class="product-description">
                                {reply[5]}
                            </div>
                        </div>
                    </div>
                </div>
            """
        else:
            history += """
                <!-- Admin Response -->
                <div class="admin-response">
                    <div class="admin-response-title">Admin Response Soon</div>
                </div>
            """

        history += f"""

            </div>
            

        """


    import header
    print(f"""
        <!--Inner Header Start-->
            <section class="wf100 p100 inner-header">
                <div class="container">
                    <h1>My History</h1>
                    <ul>
                        <li><a href="#">My Account</a></li>
                        <li><a href="#">My History</a></li>
                    </ul>
                </div>
            </section>
            
        <!--Inner Header End--> 


        <!-- Main Content -->
        <div class="container" style="margin-top:350px;">
            <h1 class="page-title">My Query History</h1>
            <p class="page-subtitle">Track all your crop-related queries and admin responses</p>

            <!-- Filter Section -->
            <div class="filter-section">
                <button class="filter-btn active">All Queries</button>
                <button class="filter-btn">Pending</button>
                <button class="filter-btn">Replied</button>
            </div>

            <!-- Query Cards -->
            {history}
            

        </div>

    """)


    print("""
    
        <style>
        
            /* Header Styles */  

            .logo {
                display: flex;
                align-items: center;
                gap: 10px;
                font-size: 20px;
                font-weight: bold;
                color: #fff;
            }

            .logo img {
                height: 50px;
                width: auto;
            }

            nav {
                display: flex;
                gap: 30px;
                align-items: center;
                flex: 1;
                margin-left: 50px;
            }

            nav a {
                color: #fff;
                text-decoration: none;
                font-weight: 500;
                transition: color 0.3s;
            }

            nav a:hover {
                color: #7ec850;
            }

            .header-right {
                display: flex;
                gap: 20px;
                align-items: center;
            }

            .ask-query-btn {
                background-color: #7ec850;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-weight: bold;
                transition: background-color 0.3s;
            }

            .ask-query-btn:hover {
                background-color: #6ab840;
            }

            .user-profile {
                color: #fff;
                font-size: 14px;
            }

            /* Main Content */
            

            .page-title {
                font-size: 32px;
                color: #2d5016;
                margin-bottom: 10px;
            }

            .page-subtitle {
                color: #666;
                margin-bottom: 30px;
                font-size: 14px;
            }

            /* Filter Section */
            .filter-section {
                display: flex;
                gap: 15px;
                margin-bottom: 30px;
                flex-wrap: wrap;
            }

            .filter-btn {
                padding: 8px 16px;
                border: 2px solid #ddd;
                background-color: #fff;
                border-radius: 20px;
                cursor: pointer;
                transition: all 0.3s;
                font-size: 14px;
            }

            .filter-btn.active {
                background-color: #2d5016;
                color: #fff;
                border-color: #2d5016;
            }

            .filter-btn:hover {
                border-color: #7ec850;
            }

            /* Query Cards */
            .query-card {
                background-color: #fff;
                border-radius: 8px;
                padding: 25px;
                margin-bottom: 25px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                border-left: 5px solid #7ec850;
            }

            .query-header {
                display: flex;
                justify-content: space-between;
                align-items: start;
                margin-bottom: 20px;
            }

            .query-title {
                font-size: 18px;
                font-weight: bold;
                color: #2d5016;
            }

            .status-badge {
                padding: 6px 14px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: bold;
                text-transform: uppercase;
            }

            .status-pending {
                background-color: #fff3cd;
                color: #856404;
            }

            .status-replied {
                background-color: #d4edda;
                color: #155724;
            }

            .query-details {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-bottom: 20px;
            }

            .detail-item {
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 6px;
            }

            .detail-label {
                font-size: 12px;
                color: #666;
                text-transform: uppercase;
                font-weight: bold;
                margin-bottom: 5px;
            }

            .detail-value {
                font-size: 14px;
                color: #333;
                font-weight: 500;
            }

            .symptoms-section {
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 6px;
                margin-bottom: 20px;
            }

            .symptoms-label {
                font-size: 12px;
                color: #666;
                text-transform: uppercase;
                font-weight: bold;
                margin-bottom: 8px;
            }

            .symptoms-text {
                font-size: 14px;
                color: #333;
                line-height: 1.6;
            }

            /* Images Section */
            .images-section {
                margin-bottom: 20px;
            }

            .images-label {
                font-size: 12px;
                color: #666;
                text-transform: uppercase;
                font-weight: bold;
                margin-bottom: 10px;
            }

            .images-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
                gap: 10px;
            }

            .image-thumbnail {
                width: 100%;
                height: 120px;
                object-fit: cover;
                border-radius: 6px;
                cursor: pointer;
                transition: transform 0.3s;
                border: 2px solid #ddd;
            }

            .image-thumbnail:hover {
                transform: scale(1.05);
                border-color: #7ec850;
            }

            /* Admin Response Section */
            .admin-response {
                background-color: #f0f8f0;
                border: 2px solid #7ec850;
                border-radius: 6px;
                padding: 20px;
                margin-top: 20px;
            }

            .admin-response-title {
                font-size: 14px;
                color: #2d5016;
                text-transform: uppercase;
                font-weight: bold;
                margin-bottom: 15px;
                display: flex;
                align-items: center;
                gap: 8px;
            }

            .admin-response-title::before {
                content: "âœ“";
                background-color: #7ec850;
                color: #fff;
                width: 24px;
                height: 24px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 12px;
            }

            .response-item {
                margin-bottom: 15px;
            }

            .response-item:last-child {
                margin-bottom: 0;
            }

            .response-label {
                font-size: 12px;
                color: #2d5016;
                text-transform: uppercase;
                font-weight: bold;
                margin-bottom: 5px;
            }

            .response-content {
                font-size: 14px;
                color: #333;
                line-height: 1.6;
                background-color: #fff;
                padding: 10px;
                border-radius: 4px;
            }

            .suggested-product {
                background-color: #fff;
                padding: 12px;
                border-radius: 4px;
                border-left: 3px solid #7ec850;
            }

            .product-name {
                font-weight: bold;
                color: #2d5016;
                margin-bottom: 5px;
            }

            .product-description {
                font-size: 13px;
                color: #666;
            }


            /* Responsive */
            @media (max-width: 768px) {
                header {
                    flex-direction: column;
                    gap: 15px;
                }

                nav {
                    margin-left: 0;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 15px;
                }

                .query-details {
                    grid-template-columns: 1fr;
                }

                
            }
        </style>     
    """)

    import footer
    
else:
    print(f"""
            <script>
                alert(" No History Founded!");
                location.href="myaccount.py?fid={FId}";
            </script>
    """)
