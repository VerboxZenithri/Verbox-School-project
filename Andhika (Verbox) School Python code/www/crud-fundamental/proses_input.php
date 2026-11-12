<?php
include "cfg.php";
?>
<?php
if ($_SERVER["REQUEST_METHOD"]=="POST"){
    $nama=$_POST["nama"];
    $kelas=$_POST["kelas"];
    $tanggal=$_POST["tanggal"];
    $sql="INSERT INTO tbsiswa (nama,kelas,Tanggal) VALUES ('$nama','$kelas','$tanggal')";
    $result=mysqli_query($conn,$sql);
    if ($result){
        header("location:doneview.php");
        exit();
    } else {echo "data gagal disimpan:" . mysqli_error($conn,$sql);}
}
?>