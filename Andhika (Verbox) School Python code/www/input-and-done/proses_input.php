<?php
include "conn.php";
?>
<?php
if ($_SERVER["REQUEST_METHOD"]=="POST"){
    $id=$_POST["id"];
    $nama=$_POST["nama"];
    $kelas=$_POST["kelas"];
    $sql="INSERT INTO tbsiswa (id,nama,kelas) VALUES ('$id','$nama','$kelas')";
    $result=mysqli_query($conn,$sql);
    if ($result){
        header("location:doneview.php");
        exit();
    } else {echo "data gagal disimpan:" . mysqli_error($conn,$sql);}
}
?>