<body>
<?php
include'cfg.php';
$id=$_GET['id'];
$sql="SELECT*FROM tbsiswa WHERE id='$id'";
$result=mysqli_query($conn, $sql);
$row=mysqli_fetch_assoc($result);
?>
<form action="process_updt.php" method="post">
    <input type="hidden"name="id"value="<?php echo$row['Id'];?>">
    <input type="text"name="nama"value="<?php echo$row['Nama'];?>"required>
    <input type="text"name="kelas"value="<?php echo$row['Kelas'];?>"required>
    <input type="date"name="tanggal"value="<?php echo$row['Tanggal'];?>"required>
    <input type="submit"value="Update Data">
</form>
</body>