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

crop_query = "SELECT * FROM crops"
mycursor.execute(crop_query)
crop = mycursor.fetchall()
crop_op= ""
part_op= ""

for cp in crop:
    crop_op += f'''
    <option value="{cp[0]}">{cp[3]}</option>
    '''

    part_query = f"SELECT * FROM parts WHERE CrpId = {cp[0]}"
    mycursor.execute(part_query)
    croppart = mycursor.fetchall()
    for part in croppart:
        part_op += f'''
        <option value="{part[0]}" data-cropid="{cp[0]}">{part[2]}</option>
        '''


    
import header
print(f"""
        <div class="page-wrapper">
            <div class="container-fluid">
                <!-- row -->
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">Disease Form</h4>
                                <form class="m-t-30" action="DiseasesBackEnd.py" method="POST" enctype="multipart/form-data"> 
                                    <div class="form-group mb-3">
                                        <label for="CropName">Crop Name</label>
                                        <select class="form-control" id="CropName" name="CropName" onchange="filterCropParts()" required>
                                            <option value="">- Select Crop -</option>
                                            {crop_op}
                                        </select>
                                    </div> 
                                    <div class="form-group mb-3">
                                        <label for="PartName">Crop Part Name</label>
                                        <select class="form-control" id="PartName" name="PartName" required>
                                            <option value="">- Select Crop Category -</option>
                                            {part_op}
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="DiseaseName">Disease Name</label>
                                        <input type="text" class="form-control" id="DiseaseName" name="DiseaseName" aria-describedby="emailHelp" required>
                                    </div>                                                        
                                    <button type="submit" class="btn btn-primary">Add Disease</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>                
            </div>
        </div>
""")

print("""

    <script>
    window.onload = function() {
        filterCropParts(); // hide irrelevant parts on page load
    };

        function filterCropParts() {
        const cropId = document.getElementById('CropName').value;
        const cropParts = document.getElementById('PartName');
        const options = cropParts.querySelectorAll('option');
        console.log(options)

        // reset selection
        cropParts.value = "";

        options.forEach(option => {
            const relatedCropId = option.getAttribute('data-cropid');
            if (!relatedCropId) return; // skip placeholder option

            // Show or hide based on selected crop ID
            if (relatedCropId === cropId) {
            option.style.display = "block";
            option.disabled = false;
            } else {
            option.style.display = "none";
            option.disabled = true;
            }
        });
        }
    </script>

""")
import footer


