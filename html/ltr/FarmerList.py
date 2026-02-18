#!C:/Python310/python.exe
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

query = "SELECT * FROM farmerlogin"
mycursor.execute(query)
myresult = mycursor.fetchall()
# print(myresult)

 
tr_html = ''
for x in myresult:
    
    block_unblock_text = "Block" if x[8] == "Active" else "Unblock"
    tr_html += f'''
    <tr>
        <td><a href="FarmerBlock.py?fid={x[0]}&status={x[9]}" title="{block_unblock_text}"><i class="fa-solid fa-ban"></i></a></td>
        <td>{x[0]}</td>
        <td><img src="assets/userImg/{x[0]}/{x[1]}" style="width: 100px; height: 100px;"></td>
        <td>{x[2]}</td>
        <td>{x[3]}</td>
        <td>{x[9]}</td>
        <td><a href="FarmerDelete.py?fid={x[0]}" onclick="return confirm('Are you sure to delete?')"><i class="fa-solid fa-trash"></i></a></td>
    </tr>
    '''
    
import header
print(f"""
        <div class="page-wrapper">
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Farmer List</h4>
                    </div>   
                </div>
            </div>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr>
                                                <th scope="col">Block</th>
                                                <th scope="col">Sr No.</th>
                                                <th scope="col">Farmer Image</th>                                                
                                                <th scope="col">Farmer Name</th>
                                                <th scope="col">Email</th>
                                                <th scope="col">Status</th>
                                                <th scope="col">Delete</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {tr_html}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                <!-- ============================================================== -->
                <!-- End PAge Content -->
                <!-- ============================================================== -->
            </div>
            <!-- ============================================================== -->
            <!-- End Container fluid  -->
            <!-- ============================================================== -->
""")
import footer
print("""
<!-- DataTables Core JS -->
<script src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.min.js"></script>

<!-- Buttons Extension JS -->
<script src="https://cdn.datatables.net/buttons/1.7.1/js/dataTables.buttons.min.js"></script>
<script src="https://cdn.datatables.net/buttons/1.7.1/js/buttons.flash.min.js"></script>
<script src="https://cdn.datatables.net/buttons/1.7.1/js/buttons.html5.min.js"></script>
<script src="https://cdn.datatables.net/buttons/1.7.1/js/buttons.print.min.js"></script>

<!-- Export File Support -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.32/pdfmake.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.32/vfs_fonts.js"></script>




<!--  Datatables-->                   
<script>
  $(document).ready(function() {
    // $('#myTable thead th').each(function () {
    //   var title = $(this).text();
    //   $(this).html('<label>' + title + '</label><br><input style="width:100px;" type="text" placeholder="Search Here" />');
    // });

    var table = $('#myTable').DataTable({
      dom: 'Bfrtip',
      buttons: [
        {
          extend: 'excelHtml5',
          title: 'Farmer List',
          filename: 'Farmer List',
          text: 'Click Here to Download Excel Report',
          orientation: 'landscape',
          pageSize: 'A4',
          exportOptions: {
            columns: [1, 3, 4, 5]
          }
        },
        {
          extend: 'print',
          text: 'Click here to Download / Print Report',
          orientation: 'landscape',
          pageSize: 'A4',
          customize: function (win) {
            $(win.document.body).css('font-size', '16pt');
            $(win.document.body).find('table').addClass('compact').css('font-size', 'inherit');
          },
          exportOptions: {
            columns: [1, 3, 4, 5]
          }
        }
      ],
      initComplete: function () {
        this.api().columns().every(function () {
          var that = this;
          $('input', this.header()).on('keyup change clear', function () {
            if (that.search() !== this.value) {
              that.search(this.value).draw();
            }
          });
        });
      }
    });

    $('.buttons-print, .buttons-excel').addClass('btn waves-effect waves-light btn-infonew');
  });
</script>
""")     