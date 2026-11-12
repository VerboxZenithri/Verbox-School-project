<?php
include'cfg.php';
if($_SERVER["REQUEST_METHOD"]=="POST"){
$id=$_POST['id'];
$nama=$_POST['nama'];
$kelas=$_POST['kelas'];
$sql="UPDATE tbsiswa SET nama='$nama',kelas='$kelas' WHERE id='$id'";
$rs=mysqli_query($conn,$sql);
if($rs){
header("Location: doneview.php");
exit();
}else{
echo"Update gagal: ".mysqli_error($conn);
}
}
?>
