<?php
include 'cfg.php';
if (isset($_GET['id'])){
    $id = $_GET['id'];
    $sql = "DELETE FROM tbsiswa WHERE id='$id'";
    $result = mysqli_query($conn, $sql);
    if ($result) {
        header("Location: doneview.php");
        exit();} 
    else {echo "Data gagal dihapus: ".mysqli_error($conn,$sql);
    }
}