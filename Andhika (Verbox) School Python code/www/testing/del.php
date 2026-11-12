<?php
include'cfg.php';
if(isset($_GET['id'])){
$id=$_GET['id'];
$sql="DELETE FROM tbsiswa WHERE id='$id'";
$rs=mysqli_query($conn,$sql);
if($rs){
header("Location: doneview.php");
exit();
}else{
echo"Data gagal dihapus: ".mysqli_error($conn);
}
}
