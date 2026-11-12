<?php
include 'cfg.php';
if ($_SERVER["REQUEST_METHOD"]=="POST"){
    $id=$_POST['id'];
    $nama=$_POST['nama'];
    $kelas=$_POST['kelas'];
    $tanggal=$_POST['tanggal'];
    $sql="UPDATE tbsiswa SET nama='$nama',kelas='$kelas',tanggal='$tanggal' WHERE id='$id'";
    $result=mysqli_query($conn,$sql);
    if($result){
        header("Location: doneview.php");
        exit();
    } else{
        echo "Update gagal: ".mysqli_error($conn);
    }
}
?>